"""
Generador de datos mockeados para la tabla Transactions de GESTOCK
Genera movimientos de inventario con patrones estacionales y temporales realistas
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from calendar import monthrange

def generate_transactions(warehouse_products_df, users_df, warehouses_df, products_df, 
                         businesses_df, months_back=6, target_transactions=1800):
    """
    Genera transacciones de inventario con patrones realistas
    
    Args:
        warehouse_products_df: DataFrame con stock inicial
        users_df: DataFrame con usuarios
        warehouses_df: DataFrame con almacenes
        products_df: DataFrame con productos
        businesses_df: DataFrame con negocios
        months_back: Meses hacia atrás desde hoy
        target_transactions: Número objetivo de transacciones
    
    Returns:
        tuple: (transactions_df, updated_warehouse_products_df)
    """
    
    # Configurar fecha de inicio y fin
    end_date = datetime.now()
    start_date = end_date - timedelta(days=months_back * 30)
    
    print(f"📅 Generando transacciones desde {start_date.strftime('%Y-%m-%d')} hasta {end_date.strftime('%Y-%m-%d')}")
    
    # Patrones estacionales por categoría (multiplicadores de actividad)
    seasonal_patterns = {
        "Alimentos": {
            1: 1.1, 2: 1.0, 3: 1.1, 4: 1.2, 5: 1.1, 6: 1.0,
            7: 1.0, 8: 1.1, 9: 1.2, 10: 1.3, 11: 1.4, 12: 1.5  # Más actividad hacia fin de año
        },
        "Ropa": {
            1: 0.8, 2: 1.0, 3: 1.3, 4: 1.2, 5: 1.1, 6: 1.0,
            7: 0.9, 8: 1.1, 9: 1.2, 10: 1.3, 11: 1.4, 12: 1.6  # Picos en marzo (escolar) y diciembre
        },
        "Electrónicos": {
            1: 0.9, 2: 1.0, 3: 1.2, 4: 1.1, 5: 1.0, 6: 1.1,
            7: 1.0, 8: 1.1, 9: 1.2, 10: 1.1, 11: 1.3, 12: 1.4  # Black Friday y Navidad
        },
        "Construcción": {
            1: 1.2, 2: 1.3, 3: 1.4, 4: 1.3, 5: 1.2, 6: 1.1,
            7: 1.0, 8: 1.1, 9: 1.2, 10: 1.3, 11: 1.2, 12: 0.8  # Temporada seca construcción
        },
        "Salud": {
            1: 1.1, 2: 1.0, 3: 1.1, 4: 1.2, 5: 1.3, 6: 1.2,
            7: 1.1, 8: 1.0, 9: 1.1, 10: 1.2, 11: 1.1, 12: 1.0  # Picos en épocas de lluvia
        },
        "Hogar": {
            1: 1.2, 2: 1.1, 3: 1.0, 4: 1.1, 5: 1.0, 6: 1.1,
            7: 1.2, 8: 1.1, 9: 1.0, 10: 1.1, 11: 1.2, 12: 1.3  # Limpieza enero y diciembre
        },
        "Oficina": {
            1: 1.4, 2: 1.3, 3: 1.2, 4: 1.1, 5: 1.0, 6: 1.1,
            7: 1.2, 8: 1.1, 9: 1.0, 10: 1.1, 11: 1.0, 12: 0.8  # Inicio de año escolar/laboral
        }
    }
    
    # Patrones por día de la semana (0=lunes, 6=domingo)
    weekly_patterns = [1.2, 1.3, 1.4, 1.3, 1.2, 0.8, 0.5]  # Menos actividad fines de semana
    
    # Tipos de transacciones y probabilidades
    transaction_types = ["ENTRADA", "SALIDA"]
    
    # Crear copia del stock para manipular
    current_stock = warehouse_products_df.copy()
    current_stock.set_index(['product_id', 'warehouse_id'], inplace=True)
    
    transactions = []
    transaction_id = 1
    
    # Generar transacciones día por día
    current_date = start_date
    daily_transaction_target = target_transactions / (months_back * 30)
    
    while current_date <= end_date:
        # Ajustar por día de la semana
        weekday_multiplier = weekly_patterns[current_date.weekday()]
        
        # Calcular transacciones para este día
        daily_transactions = max(1, int(daily_transaction_target * weekday_multiplier * random.uniform(0.7, 1.3)))
        
        # Generar transacciones para este día
        for _ in range(daily_transactions):
            # Seleccionar warehouse_product aleatorio
            available_stock_records = current_stock[current_stock['stock'] > 0].copy()
            
            if len(available_stock_records) == 0:
                continue
            
            # Seleccionar registro de stock
            stock_record_idx = random.choice(available_stock_records.index)
            product_id, warehouse_id = stock_record_idx
            
            # Obtener información adicional
            product_info = products_df[products_df['id'] == product_id].iloc[0]
            warehouse_info = warehouses_df[warehouses_df['id'] == warehouse_id].iloc[0]
            business_info = businesses_df[businesses_df['id'] == warehouse_info['business_id']].iloc[0]
            
            # Aplicar patrón estacional
            month = current_date.month
            category = product_info['category']
            seasonal_multiplier = seasonal_patterns.get(category, {}).get(month, 1.0)
            
            # Decidir tipo de transacción
            current_stock_level = current_stock.loc[stock_record_idx, 'stock']
            min_stock = current_stock.loc[stock_record_idx, 'min_stock']
            max_stock = current_stock.loc[stock_record_idx, 'max_stock']
            
            # Lógica para tipo de transacción
            if current_stock_level <= min_stock:
                # Stock bajo -> mayor probabilidad de ENTRADA
                transaction_type = "ENTRADA" if random.random() < 0.8 else "SALIDA"
            elif current_stock_level >= max_stock * 0.8:
                # Stock alto -> mayor probabilidad de SALIDA
                transaction_type = "SALIDA" if random.random() < 0.7 else "ENTRADA"
            else:
                # Stock normal -> balanceado con sesgo hacia SALIDA (más ventas que compras)
                transaction_type = "SALIDA" if random.random() < 0.6 else "ENTRADA"
            
            # Ajustar probabilidad por estacionalidad
            if seasonal_multiplier > 1.2 and transaction_type == "SALIDA":
                # En temporada alta, más salidas
                pass
            elif seasonal_multiplier > 1.2 and transaction_type == "ENTRADA":
                # En temporada alta, también más reposición
                pass
            
            # Calcular cantidad
            if transaction_type == "ENTRADA":
                # Cantidad de entrada basada en reposición
                ideal_stock = (min_stock + max_stock) // 2
                quantity = random.randint(
                    max(1, min_stock),
                    max(min_stock + 1, ideal_stock)
                )
            else:  # SALIDA
                # Cantidad de salida limitada por stock actual
                max_sale = min(current_stock_level, max(1, current_stock_level // 3))
                quantity = random.randint(1, max(1, max_sale))
            
            # Aplicar modificador estacional a cantidad
            quantity = max(1, int(quantity * seasonal_multiplier * random.uniform(0.8, 1.2)))
            
            # Validar transacción de SALIDA
            if transaction_type == "SALIDA" and quantity > current_stock_level:
                quantity = current_stock_level
                
            if transaction_type == "SALIDA" and current_stock_level <= 0:
                continue  # Skip si no hay stock
            
            # Seleccionar usuario del mismo negocio
            business_users = users_df[
                (users_df['business_id'] == business_info['id']) & 
                (users_df['is_active'] == True)
            ]
            
            if len(business_users) == 0:
                continue
                
            user = business_users.sample(1).iloc[0]
            
            # Generar descripción realista
            descriptions = {
                "ENTRADA": [
                    f"Compra a proveedor {product_info['supplier']}",
                    f"Reposición de stock - {product_info['name']}",
                    f"Entrada por compra mayorista",
                    f"Recepción de mercancía - Pedido #{random.randint(1000, 9999)}",
                    f"Reabastecimiento {warehouse_info['name']}",
                    f"Compra directa - {product_info['supplier']}"
                ],
                "SALIDA": [
                    f"Venta al cliente - Pedido #{random.randint(1000, 9999)}",
                    f"Salida por venta mostrador",
                    f"Entrega a cliente - {product_info['name']}",
                    f"Venta corporativa",
                    f"Despacho desde {warehouse_info['name']}",
                    f"Salida por venta directa",
                    f"Entrega domicilio - Cliente #{random.randint(100, 999)}"
                ]
            }
            
            description = random.choice(descriptions[transaction_type])
            
            # Crear transacción
            transaction = {
                'id': transaction_id,
                'type': transaction_type,
                'quantity': quantity,
                'description': description,
                'created_at': current_date + timedelta(
                    hours=random.randint(8, 18),
                    minutes=random.randint(0, 59)
                ),
                'user_id': user['id'],
                'product_id': product_id,
                'warehouse_id': warehouse_id,
                'product_name': product_info['name'],
                'product_category': product_info['category'],
                'warehouse_name': warehouse_info['name'],
                'business_id': business_info['id'],
                'user_name': user['full_name']
            }
            
            transactions.append(transaction)
            
            # Actualizar stock actual
            if transaction_type == "ENTRADA":
                current_stock.loc[stock_record_idx, 'stock'] += quantity
            else:  # SALIDA
                current_stock.loc[stock_record_idx, 'stock'] -= quantity
                current_stock.loc[stock_record_idx, 'stock'] = max(0, current_stock.loc[stock_record_idx, 'stock'])
            
            transaction_id += 1
        
        # Avanzar al siguiente día
        current_date += timedelta(days=1)
        
        # Progreso cada 10 días
        if (current_date - start_date).days % 10 == 0:
            progress = (current_date - start_date).days / (months_back * 30) * 100
            print(f"  📈 Progreso: {progress:.1f}% - {len(transactions)} transacciones generadas")
    
    # Convertir a DataFrame
    transactions_df = pd.DataFrame(transactions)
    
    # Resetear índice del stock actualizado
    updated_stock = current_stock.reset_index()
    
    return transactions_df, updated_stock

def generate_transaction_summary(transactions_df):
    """
    Genera resumen de las transacciones generadas
    """
    print(f"\n📊 RESUMEN DE TRANSACCIONES GENERADAS:")
    print("="*50)
    
    total_transactions = len(transactions_df)
    print(f"📝 Total transacciones: {total_transactions:,}")
    
    # Por tipo
    type_summary = transactions_df['type'].value_counts()
    print(f"\n📈 Por tipo:")
    for t_type, count in type_summary.items():
        percentage = (count / total_transactions) * 100
        print(f"  {t_type}: {count:,} ({percentage:.1f}%)")
    
    # Por mes
    transactions_df['month'] = pd.to_datetime(transactions_df['created_at']).dt.to_period('M')
    monthly_summary = transactions_df['month'].value_counts().sort_index()
    print(f"\n📅 Por mes:")
    for month, count in monthly_summary.items():
        print(f"  {month}: {count:,} transacciones")
    
    # Por categoría
    category_summary = transactions_df['product_category'].value_counts()
    print(f"\n📦 Por categoría de producto:")
    for category, count in category_summary.items():
        percentage = (count / total_transactions) * 100
        print(f"  {category}: {count:,} ({percentage:.1f}%)")
    
    # Por negocio
    business_summary = transactions_df['business_id'].value_counts().sort_index()
    print(f"\n🏢 Por negocio:")
    for business_id, count in business_summary.items():
        percentage = (count / total_transactions) * 100
        print(f"  Negocio {business_id}: {count:,} ({percentage:.1f}%)")

def save_transactions_csv(transactions_df, updated_stock_df):
    """
    Guarda los archivos CSV de transacciones y stock actualizado
    """
    # Guardar transacciones
    transactions_filepath = '../raw/transactions.csv'
    transactions_df.to_csv(transactions_filepath, index=False, encoding='utf-8')
    print(f"\n✅ Archivo transactions.csv guardado con {len(transactions_df)} transacciones")
    
    # Actualizar stock
    stock_filepath = '../raw/warehouse_products.csv'
    updated_stock_df.to_csv(stock_filepath, index=False, encoding='utf-8')
    print(f"✅ Archivo warehouse_products.csv actualizado con stock final")

if __name__ == "__main__":
    # Cargar datos base
    try:
        warehouse_products_df = pd.read_csv('../raw/warehouse_products.csv')
        users_df = pd.read_csv('../raw/users.csv')
        warehouses_df = pd.read_csv('../raw/warehouses.csv')
        products_df = pd.read_csv('../raw/products.csv')
        businesses_df = pd.read_csv('../raw/businesses.csv')
        
        print(f"📋 Datos cargados:")
        print(f"  - {len(warehouse_products_df)} registros de stock")
        print(f"  - {len(users_df)} usuarios")
        print(f"  - {len(warehouses_df)} almacenes")
        print(f"  - {len(products_df)} productos")
        print(f"  - {len(businesses_df)} negocios")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Primero debe ejecutar los generadores previos")
        exit(1)
    
    # Generar transacciones
    transactions_df, updated_stock_df = generate_transactions(
        warehouse_products_df, users_df, warehouses_df, 
        products_df, businesses_df, months_back=6, target_transactions=1800
    )
    
    # Generar resumen
    generate_transaction_summary(transactions_df)
    
    # Guardar archivos
    save_transactions_csv(transactions_df, updated_stock_df)