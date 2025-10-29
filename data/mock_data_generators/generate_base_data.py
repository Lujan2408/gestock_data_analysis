"""
Script maestro para generar todos los datos base del proyecto GESTOCK
Ejecuta todos los generadores y valida la integridad de los datos
"""

import pandas as pd
import os
import sys
from datetime import datetime

# Importar los generadores
from generate_businesses import generate_businesses, save_businesses_csv
from generate_products import generate_products, save_products_csv
from generate_warehouses import generate_warehouses, save_warehouses_csv

def validate_data_integrity(businesses_df, products_df, warehouses_df):
    """
    Valida la integridad de los datos generados
    
    Args:
        businesses_df (pandas.DataFrame): DataFrame de negocios
        products_df (pandas.DataFrame): DataFrame de productos
        warehouses_df (pandas.DataFrame): DataFrame de almacenes
    
    Returns:
        bool: True si todos los datos son válidos
    """
    
    print("\n🔍 VALIDANDO INTEGRIDAD DE DATOS...")
    print("="*50)
    
    errors = []
    warnings = []
    
    # Validar negocios
    if businesses_df['id'].duplicated().any():
        errors.append("❌ IDs duplicados en businesses")
    
    if businesses_df['name'].duplicated().any():
        warnings.append("⚠️ Nombres duplicados en businesses")
    
    # Validar productos
    if products_df['id'].duplicated().any():
        errors.append("❌ IDs duplicados en products")
    
    if len(products_df) == 0:
        errors.append("❌ No se generaron productos")
    
    # Validar precios
    if (products_df['price'] <= 0).any():
        errors.append("❌ Precios negativos o cero en products")
    
    if (products_df['cost_price'] <= 0).any():
        errors.append("❌ Costos negativos o cero en products")
    
    if (products_df['cost_price'] >= products_df['price']).any():
        warnings.append("⚠️ Algunos productos tienen costo mayor al precio de venta")
    
    # Validar almacenes
    if warehouses_df['id'].duplicated().any():
        errors.append("❌ IDs duplicados en warehouses")
    
    # Validar relaciones
    business_ids = set(businesses_df['id'])
    warehouse_business_ids = set(warehouses_df['business_id'])
    
    if not warehouse_business_ids.issubset(business_ids):
        errors.append("❌ Almacenes con business_id inexistentes")
    
    # Validar que cada negocio tenga al menos un almacén
    businesses_without_warehouses = business_ids - warehouse_business_ids
    if businesses_without_warehouses:
        warnings.append(f"⚠️ Negocios sin almacenes: {businesses_without_warehouses}")
    
    # Mostrar resultados de validación
    if errors:
        print("ERRORES ENCONTRADOS:")
        for error in errors:
            print(f"  {error}")
        return False
    
    if warnings:
        print("ADVERTENCIAS:")
        for warning in warnings:
            print(f"  {warning}")
    
    if not errors and not warnings:
        print("✅ Todos los datos son válidos")
    
    return True

def generate_summary_report(businesses_df, products_df, warehouses_df):
    """
    Genera un reporte resumen de los datos generados
    """
    
    print("\n📊 REPORTE RESUMEN DE DATOS GENERADOS")
    print("="*50)
    
    # Resumen general
    print(f"🏢 Negocios generados: {len(businesses_df)}")
    print(f"📦 Productos generados: {len(products_df)}")
    print(f"🏭 Almacenes generados: {len(warehouses_df)}")
    
    # Distribución por industria
    print(f"\n📈 Distribución por industria:")
    industry_dist = businesses_df['industry'].value_counts()
    for industry, count in industry_dist.items():
        print(f"  {industry}: {count} negocios")
    
    # Distribución por categoría de productos
    print(f"\n📦 Distribución por categoría de productos:")
    category_dist = products_df['category'].value_counts()
    for category, count in category_dist.items():
        print(f"  {category}: {count} productos")
    
    # Almacenes por negocio
    print(f"\n🏭 Almacenes por negocio:")
    warehouses_per_business = warehouses_df['business_id'].value_counts().sort_index()
    for business_id, count in warehouses_per_business.items():
        business_name = businesses_df[businesses_df['id'] == business_id]['name'].iloc[0]
        print(f"  {business_name}: {count} almacenes")
    
    # Estadísticas de precios
    print(f"\n💰 Estadísticas de precios:")
    print(f"  Precio promedio: ${products_df['price'].mean():,.0f}")
    print(f"  Precio mínimo: ${products_df['price'].min():,.0f}")
    print(f"  Precio máximo: ${products_df['price'].max():,.0f}")
    
    # Margen de ganancia promedio
    print(f"  Margen promedio: {products_df['profit_margin'].mean():.1f}%")
    
    print(f"\n📅 Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """
    Función principal que ejecuta todo el proceso de generación
    """
    
    print("🚀 INICIANDO GENERACIÓN DE DATOS BASE GESTOCK")
    print("="*60)
    
    try:
        # Cambiar al directorio correcto
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # Generar negocios
        print("\n1️⃣ Generando negocios...")
        businesses_df = generate_businesses(8)
        save_businesses_csv(businesses_df)
        
        # Generar productos  
        print("\n2️⃣ Generando productos...")
        products_df = generate_products(85)
        save_products_csv(products_df)
        
        # Generar almacenes
        print("\n3️⃣ Generando almacenes...")
        warehouses_df = generate_warehouses(businesses_df)
        save_warehouses_csv(warehouses_df)
        
        # Validar integridad
        if validate_data_integrity(businesses_df, products_df, warehouses_df):
            print("\n✅ GENERACIÓN EXITOSA")
        else:
            print("\n❌ GENERACIÓN CON ERRORES")
            return False
        
        # Generar reporte
        generate_summary_report(businesses_df, products_df, warehouses_df)
        
        print(f"\n🎉 PROCESO COMPLETADO")
        print(f"📁 Archivos generados en: ../raw/")
        print(f"   - businesses.csv")
        print(f"   - products.csv") 
        print(f"   - warehouses.csv")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR durante la generación: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)