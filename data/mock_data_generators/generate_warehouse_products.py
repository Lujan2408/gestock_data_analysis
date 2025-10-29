"""
Generador de datos mockeados para la tabla WarehouseProducts de GESTOCK
Asigna productos a almacenes con stock inicial realista
"""

import pandas as pd
import random
from datetime import datetime

def generate_warehouse_products(businesses_df, warehouses_df, products_df):
    """
    Genera datos mockeados para stock inicial de productos en almacenes
    
    Args:
        businesses_df (pandas.DataFrame): DataFrame con datos de negocios
        warehouses_df (pandas.DataFrame): DataFrame con datos de almacenes  
        products_df (pandas.DataFrame): DataFrame con datos de productos
    
    Returns:
        pandas.DataFrame: DataFrame con stock por almacén
    """
    
    # Configuración de stock por tipo de negocio y categoría
    stock_config = {
        "Supermercado": {
            "Alimentos": {"min_stock": 50, "max_stock": 500, "probability": 0.9},
            "Hogar": {"min_stock": 20, "max_stock": 150, "probability": 0.8},
            "Salud": {"min_stock": 10, "max_stock": 80, "probability": 0.6},
            "Oficina": {"min_stock": 5, "max_stock": 50, "probability": 0.4},
            "default": {"min_stock": 5, "max_stock": 30, "probability": 0.3}
        },
        "Farmacia": {
            "Salud": {"min_stock": 30, "max_stock": 200, "probability": 0.95},
            "Hogar": {"min_stock": 10, "max_stock": 80, "probability": 0.7},
            "Alimentos": {"min_stock": 5, "max_stock": 40, "probability": 0.5},
            "default": {"min_stock": 2, "max_stock": 20, "probability": 0.2}
        },
        "Ferretería": {
            "Construcción": {"min_stock": 20, "max_stock": 300, "probability": 0.9},
            "Hogar": {"min_stock": 15, "max_stock": 100, "probability": 0.8},
            "Electrónicos": {"min_stock": 5, "max_stock": 50, "probability": 0.6},
            "default": {"min_stock": 3, "max_stock": 25, "probability": 0.3}
        },
        "Librería": {
            "Oficina": {"min_stock": 25, "max_stock": 200, "probability": 0.9},
            "Electrónicos": {"min_stock": 5, "max_stock": 40, "probability": 0.6},
            "default": {"min_stock": 3, "max_stock": 30, "probability": 0.4}
        },
        "Tienda de Electrónicos": {
            "Electrónicos": {"min_stock": 10, "max_stock": 100, "probability": 0.95},
            "Oficina": {"min_stock": 5, "max_stock": 60, "probability": 0.7},
            "default": {"min_stock": 2, "max_stock": 20, "probability": 0.3}
        },
        "Boutique": {
            "Ropa": {"min_stock": 15, "max_stock": 150, "probability": 0.9},
            "default": {"min_stock": 2, "max_stock": 25, "probability": 0.2}
        },
        "Almacén Mayorista": {
            "Alimentos": {"min_stock": 100, "max_stock": 1000, "probability": 0.8},
            "Ropa": {"min_stock": 50, "max_stock": 500, "probability": 0.8},
            "Electrónicos": {"min_stock": 30, "max_stock": 200, "probability": 0.7},
            "Construcción": {"min_stock": 50, "max_stock": 800, "probability": 0.7},
            "Hogar": {"min_stock": 40, "max_stock": 300, "probability": 0.7},
            "default": {"min_stock": 20, "max_stock": 200, "probability": 0.6}
        },
        "Distribuidora": {
            "Alimentos": {"min_stock": 200, "max_stock": 2000, "probability": 0.9},
            "Ropa": {"min_stock": 100, "max_stock": 800, "probability": 0.8},
            "Electrónicos": {"min_stock": 50, "max_stock": 400, "probability": 0.8},
            "Construcción": {"min_stock": 80, "max_stock": 1200, "probability": 0.8},
            "Hogar": {"min_stock": 60, "max_stock": 500, "probability": 0.7},
            "Salud": {"min_stock": 40, "max_stock": 300, "probability": 0.7},
            "default": {"min_stock": 30, "max_stock": 300, "probability": 0.6}
        }
    }
    
    warehouse_products = []
    
    # Procesar cada negocio
    for _, business in businesses_df.iterrows():
        business_id = business['id']
        business_type = business['business_type']
        
        # Obtener almacenes de este negocio
        business_warehouses = warehouses_df[warehouses_df['business_id'] == business_id]
        
        # Configuración de stock para este tipo de negocio
        business_stock_config = stock_config.get(business_type, {
            "default": {"min_stock": 10, "max_stock": 100, "probability": 0.5}
        })
        
        print(f"📦 Procesando {business['name']} ({business_type}) - {len(business_warehouses)} almacenes")
        
        # Para cada almacén de este negocio
        for _, warehouse in business_warehouses.iterrows():
            warehouse_id = warehouse['id']
            warehouse_name = warehouse['name']
            
            products_in_warehouse = 0
            
            # Evaluar cada producto
            for _, product in products_df.iterrows():
                product_id = product['id']
                product_category = product['category']
                
                # Obtener configuración para esta categoría
                category_config = business_stock_config.get(
                    product_category, 
                    business_stock_config.get("default", {"min_stock": 5, "max_stock": 50, "probability": 0.3})
                )
                
                # Decidir si este producto estará en este almacén
                if random.random() <= category_config["probability"]:
                    # Calcular stock inicial
                    min_stock = category_config["min_stock"]
                    max_stock = category_config["max_stock"]
                    
                    # Ajustar stock según el tamaño del negocio
                    if business['size'] == 'Grande':
                        min_stock = int(min_stock * 1.5)
                        max_stock = int(max_stock * 1.8)
                    elif business['size'] == 'Pequeña':
                        min_stock = int(min_stock * 0.6)
                        max_stock = int(max_stock * 0.7)
                    
                    # Evitar stocks muy bajos
                    min_stock = max(1, min_stock)
                    max_stock = max(min_stock + 1, max_stock)
                    
                    initial_stock = random.randint(min_stock, max_stock)
                    
                    # Crear registro de stock
                    warehouse_product = {
                        'product_id': product_id,
                        'warehouse_id': warehouse_id,
                        'stock': initial_stock,
                        'min_stock': max(1, min_stock // 4),  # Stock mínimo para alertas
                        'max_stock': max_stock,
                        'last_updated': datetime.now() - pd.Timedelta(days=random.randint(1, 30))
                    }
                    
                    warehouse_products.append(warehouse_product)
                    products_in_warehouse += 1
            
            print(f"  └── {warehouse_name}: {products_in_warehouse} productos asignados")
    
    return pd.DataFrame(warehouse_products)

def generate_stock_summary(warehouse_products_df, businesses_df, warehouses_df, products_df):
    """
    Genera un resumen del stock generado
    """
    print(f"\n📊 RESUMEN DE STOCK GENERADO:")
    print("="*50)
    
    # Estadísticas generales
    total_records = len(warehouse_products_df)
    total_stock_units = warehouse_products_df['stock'].sum()
    
    print(f"📦 Total registros de stock: {total_records:,}")
    print(f"📦 Total unidades en stock: {total_stock_units:,}")
    print(f"📦 Stock promedio por producto-almacén: {warehouse_products_df['stock'].mean():.1f}")
    
    # Stock por negocio
    print(f"\n🏢 Stock por negocio:")
    
    # Unir datos para obtener información del negocio
    stock_with_warehouse = warehouse_products_df.merge(warehouses_df[['id', 'business_id']], 
                                                       left_on='warehouse_id', right_on='id')
    stock_by_business = stock_with_warehouse.groupby('business_id').agg({
        'stock': ['sum', 'count', 'mean']
    }).round(1)
    
    for business_id in sorted(stock_by_business.index):
        business_name = businesses_df[businesses_df['id'] == business_id]['name'].iloc[0]
        total_stock = stock_by_business.loc[business_id, ('stock', 'sum')]
        product_count = stock_by_business.loc[business_id, ('stock', 'count')]
        avg_stock = stock_by_business.loc[business_id, ('stock', 'mean')]
        
        print(f"  {business_name}: {total_stock:,.0f} unidades ({product_count} productos, avg: {avg_stock:.1f})")
    
    # Stock por categoría
    print(f"\n📋 Stock por categoría de producto:")
    
    stock_with_product = warehouse_products_df.merge(products_df[['id', 'category']], 
                                                    left_on='product_id', right_on='id')
    stock_by_category = stock_with_product.groupby('category')['stock'].agg(['sum', 'count', 'mean']).round(1)
    
    for category in stock_by_category.index:
        total_stock = stock_by_category.loc[category, 'sum']
        product_count = stock_by_category.loc[category, 'count']
        avg_stock = stock_by_category.loc[category, 'mean']
        
        print(f"  {category}: {total_stock:,.0f} unidades ({product_count} asignaciones, avg: {avg_stock:.1f})")

def save_warehouse_products_csv(df, filename='warehouse_products.csv'):
    """
    Guarda el DataFrame de stock en un archivo CSV
    """
    filepath = f'../raw/{filename}'
    df.to_csv(filepath, index=False, encoding='utf-8')
    print(f"\n✅ Archivo {filename} guardado con {len(df)} registros de stock")

if __name__ == "__main__":
    # Cargar datos base
    try:
        businesses_df = pd.read_csv('../raw/businesses.csv')
        warehouses_df = pd.read_csv('../raw/warehouses.csv')
        products_df = pd.read_csv('../raw/products.csv')
        
        print(f"📋 Datos cargados:")
        print(f"  - {len(businesses_df)} negocios")
        print(f"  - {len(warehouses_df)} almacenes")
        print(f"  - {len(products_df)} productos")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Primero debe ejecutar generate_base_data.py")
        exit(1)
    
    # Generar stock
    warehouse_products_df = generate_warehouse_products(
        businesses_df, warehouses_df, products_df
    )
    
    # Generar resumen
    generate_stock_summary(warehouse_products_df, businesses_df, warehouses_df, products_df)
    
    # Guardar archivo
    save_warehouse_products_csv(warehouse_products_df)