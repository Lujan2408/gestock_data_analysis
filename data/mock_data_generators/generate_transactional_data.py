"""
Script maestro para generar todos los datos transaccionales del proyecto GESTOCK
Coordina la generación de usuarios, stock y transacciones con validación de reglas de negocio
"""

import pandas as pd
import os
import sys
from datetime import datetime

# Importar los generadores transaccionales
from generate_users import generate_users, save_users_csv
from generate_warehouse_products import generate_warehouse_products, save_warehouse_products_csv
from generate_transactions import generate_transactions, save_transactions_csv

def validate_transactional_data(users_df, warehouse_products_df, transactions_df, 
                               businesses_df, warehouses_df, products_df):
    """
    Valida la integridad de los datos transaccionales generados
    
    Returns:
        bool: True si todos los datos son válidos
    """
    
    print("\n🔍 VALIDANDO INTEGRIDAD DE DATOS TRANSACCIONALES...")
    print("="*60)
    
    errors = []
    warnings = []
    
    # Validar usuarios
    print("👥 Validando usuarios...")
    if users_df['id'].duplicated().any():
        errors.append("❌ IDs duplicados en users")
    
    if users_df['email'].duplicated().any():
        errors.append("❌ Emails duplicados en users")
    
    # Validar que cada negocio tenga al menos un usuario activo
    active_users_per_business = users_df[users_df['is_active'] == True].groupby('business_id').size()
    businesses_without_active_users = set(businesses_df['id']) - set(active_users_per_business.index)
    
    if businesses_without_active_users:
        warnings.append(f"⚠️ Negocios sin usuarios activos: {businesses_without_active_users}")
    
    # Validar stock inicial
    print("📦 Validando stock inicial...")
    if warehouse_products_df['stock'].isna().any():
        errors.append("❌ Valores nulos en stock")
    
    if (warehouse_products_df['stock'] < 0).any():
        errors.append("❌ Stock negativo encontrado")
    
    # Validar relaciones de stock
    warehouse_ids = set(warehouses_df['id'])
    product_ids = set(products_df['id'])
    stock_warehouse_ids = set(warehouse_products_df['warehouse_id'])
    stock_product_ids = set(warehouse_products_df['product_id'])
    
    if not stock_warehouse_ids.issubset(warehouse_ids):
        errors.append("❌ Stock con warehouse_id inexistentes")
    
    if not stock_product_ids.issubset(product_ids):
        errors.append("❌ Stock con product_id inexistentes")
    
    # Validar transacciones
    print("📊 Validando transacciones...")
    if len(transactions_df) == 0:
        errors.append("❌ No se generaron transacciones")
    
    if transactions_df['id'].duplicated().any():
        errors.append("❌ IDs duplicados en transactions")
    
    # Validar tipos de transacción
    valid_types = {'ENTRADA', 'SALIDA'}
    invalid_types = set(transactions_df['type']) - valid_types
    if invalid_types:
        errors.append(f"❌ Tipos de transacción inválidos: {invalid_types}")
    
    # Validar cantidades
    if (transactions_df['quantity'] <= 0).any():
        errors.append("❌ Cantidades negativas o cero en transactions")
    
    # Validar relaciones de transacciones
    transaction_user_ids = set(transactions_df['user_id'])
    transaction_product_ids = set(transactions_df['product_id'])
    transaction_warehouse_ids = set(transactions_df['warehouse_id'])
    
    user_ids = set(users_df['id'])
    
    if not transaction_user_ids.issubset(user_ids):
        errors.append("❌ Transacciones con user_id inexistentes")
    
    if not transaction_product_ids.issubset(product_ids):
        errors.append("❌ Transacciones con product_id inexistentes")
    
    if not transaction_warehouse_ids.issubset(warehouse_ids):
        errors.append("❌ Transacciones con warehouse_id inexistentes")
    
    # Validar coherencia de negocio
    print("🏢 Validando coherencia de negocio...")
    
    # Verificar que las transacciones son de usuarios del mismo negocio que el almacén
    # Obtener business_id de almacenes
    warehouses_business = warehouses_df[['id', 'business_id']].rename(columns={
        'id': 'warehouse_id', 
        'business_id': 'warehouse_business_id'
    })
    
    # Obtener business_id de usuarios
    users_business = users_df[['id', 'business_id']].rename(columns={
        'id': 'user_id', 
        'business_id': 'user_business_id'
    })
    
    # Combinar con transacciones
    transaction_details = transactions_df.merge(
        warehouses_business, on='warehouse_id', how='left'
    ).merge(
        users_business, on='user_id', how='left'
    )
    
    business_mismatch = transaction_details[
        transaction_details['warehouse_business_id'] != transaction_details['user_business_id']
    ]
    
    if len(business_mismatch) > 0:
        errors.append(f"❌ {len(business_mismatch)} transacciones con usuarios de diferente negocio que el almacén")
    
    # Validar fechas
    transactions_df['created_at'] = pd.to_datetime(transactions_df['created_at'])
    if transactions_df['created_at'].isna().any():
        errors.append("❌ Fechas inválidas en transactions")
    
    # Mostrar resultados de validación
    print("\n📋 RESULTADOS DE VALIDACIÓN:")
    print("-" * 40)
    
    if errors:
        print("❌ ERRORES ENCONTRADOS:")
        for error in errors:
            print(f"  {error}")
    
    if warnings:
        print("⚠️ ADVERTENCIAS:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors and not warnings:
        print("✅ Todos los datos transaccionales son válidos")
    elif not errors:
        print("✅ Datos válidos (con advertencias menores)")
    
    return len(errors) == 0

def generate_comprehensive_summary(users_df, warehouse_products_df, transactions_df, 
                                 businesses_df, warehouses_df, products_df):
    """
    Genera un reporte completo de todos los datos generados
    """
    
    print("\n📊 REPORTE COMPLETO DE DATOS GESTOCK")
    print("="*60)
    
    # Resumen general
    print("📈 RESUMEN GENERAL:")
    print(f"  🏢 Negocios: {len(businesses_df)}")
    print(f"  🏭 Almacenes: {len(warehouses_df)}")
    print(f"  📦 Productos: {len(products_df)}")
    print(f"  👥 Usuarios: {len(users_df)}")
    print(f"  📊 Registros de stock: {len(warehouse_products_df):,}")
    print(f"  💱 Transacciones: {len(transactions_df):,}")
    
    # Análisis por negocio
    print(f"\n🏢 ANÁLISIS POR NEGOCIO:")
    for _, business in businesses_df.iterrows():
        business_id = business['id']
        business_name = business['name']
        business_type = business['business_type']
        
        # Contadores
        business_warehouses = len(warehouses_df[warehouses_df['business_id'] == business_id])
        business_users = len(users_df[users_df['business_id'] == business_id])
        business_stock_records = len(warehouse_products_df[
            warehouse_products_df['warehouse_id'].isin(
                warehouses_df[warehouses_df['business_id'] == business_id]['id']
            )
        ])
        business_transactions = len(transactions_df[transactions_df['business_id'] == business_id])
        
        print(f"  {business_name} ({business_type}):")
        print(f"    - Almacenes: {business_warehouses}")
        print(f"    - Usuarios: {business_users}")
        print(f"    - Productos en stock: {business_stock_records}")
        print(f"    - Transacciones: {business_transactions}")
    
    # Estadísticas de transacciones
    print(f"\n💱 ESTADÍSTICAS DE TRANSACCIONES:")
    
    # Por tipo
    type_counts = transactions_df['type'].value_counts()
    total_transactions = len(transactions_df)
    
    for t_type, count in type_counts.items():
        percentage = (count / total_transactions) * 100
        print(f"  {t_type}: {count:,} ({percentage:.1f}%)")
    
    # Período de datos
    min_date = transactions_df['created_at'].min()
    max_date = transactions_df['created_at'].max()
    print(f"  Período: {min_date.strftime('%Y-%m-%d')} a {max_date.strftime('%Y-%m-%d')}")
    
    # Volumen de unidades
    total_entries = transactions_df[transactions_df['type'] == 'ENTRADA']['quantity'].sum()
    total_exits = transactions_df[transactions_df['type'] == 'SALIDA']['quantity'].sum()
    
    print(f"  Total unidades ingresadas: {total_entries:,}")
    print(f"  Total unidades vendidas: {total_exits:,}")
    print(f"  Balance neto: {total_entries - total_exits:,}")
    
    # Stock actual
    current_total_stock = warehouse_products_df['stock'].sum()
    print(f"  Stock actual total: {current_total_stock:,} unidades")
    
    # Valor del inventario
    stock_with_products = warehouse_products_df.merge(
        products_df[['id', 'price']], left_on='product_id', right_on='id'
    )
    total_inventory_value = (stock_with_products['stock'] * stock_with_products['price']).sum()
    print(f"  Valor total del inventario: ${total_inventory_value:,.0f}")
    
    print(f"\n📅 Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """
    Función principal que ejecuta todo el proceso de generación transaccional
    """
    
    print("🚀 INICIANDO GENERACIÓN DE DATOS TRANSACCIONALES GESTOCK")
    print("="*70)
    
    try:
        # Cambiar al directorio correcto
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # Cargar datos base
        print("📋 Cargando datos base...")
        businesses_df = pd.read_csv('../raw/businesses.csv')
        warehouses_df = pd.read_csv('../raw/warehouses.csv')
        products_df = pd.read_csv('../raw/products.csv')
        
        print(f"  ✅ {len(businesses_df)} negocios")
        print(f"  ✅ {len(warehouses_df)} almacenes")
        print(f"  ✅ {len(products_df)} productos")
        
        # Generar usuarios
        print("\n1️⃣ Generando usuarios...")
        users_df = generate_users(businesses_df)
        save_users_csv(users_df)
        
        # Generar stock inicial
        print("\n2️⃣ Generando stock inicial...")
        warehouse_products_df = generate_warehouse_products(businesses_df, warehouses_df, products_df)
        save_warehouse_products_csv(warehouse_products_df)
        
        # Generar transacciones
        print("\n3️⃣ Generando transacciones...")
        transactions_df, updated_stock_df = generate_transactions(
            warehouse_products_df, users_df, warehouses_df, 
            products_df, businesses_df, months_back=6, target_transactions=1800
        )
        
        save_transactions_csv(transactions_df, updated_stock_df)
        
        # Usar el stock actualizado para validaciones
        warehouse_products_df = updated_stock_df
        
        # Validar integridad
        if validate_transactional_data(users_df, warehouse_products_df, transactions_df,
                                     businesses_df, warehouses_df, products_df):
            print("\n✅ GENERACIÓN TRANSACCIONAL EXITOSA")
        else:
            print("\n❌ GENERACIÓN CON ERRORES")
            return False
        
        # Generar reporte completo
        generate_comprehensive_summary(users_df, warehouse_products_df, transactions_df,
                                     businesses_df, warehouses_df, products_df)
        
        print(f"\n🎉 PROCESO TRANSACCIONAL COMPLETADO")
        print(f"📁 Archivos actualizados en: ../raw/")
        print(f"   - users.csv ({len(users_df)} usuarios)")
        print(f"   - warehouse_products.csv ({len(warehouse_products_df)} registros de stock)")
        print(f"   - transactions.csv ({len(transactions_df)} transacciones)")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR durante la generación transaccional: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)