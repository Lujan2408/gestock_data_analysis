"""
Generador de datos mockeados para la tabla Warehouses de GESTOCK
Crea almacenes distribuidos entre negocios con ubicaciones realistas
"""

import pandas as pd
import random
from datetime import datetime, timedelta

def generate_warehouses(businesses_df, warehouses_per_business_range=(2, 4)):
    """
    Genera datos mockeados para almacenes basados en los negocios existentes
    
    Args:
        businesses_df (pandas.DataFrame): DataFrame con datos de negocios
        warehouses_per_business_range (tuple): Rango de almacenes por negocio
    
    Returns:
        pandas.DataFrame: DataFrame con datos de almacenes
    """
    
    # Tipos de almacenes según el tipo de negocio
    warehouse_types = {
        "Supermercado": ["Almacén Principal", "Bodega Refrigerados", "Depósito Secos"],
        "Farmacia": ["Almacén Medicamentos", "Bodega General", "Refrigerados"],
        "Ferretería": ["Bodega Principal", "Almacén Herramientas", "Depósito Materiales"],
        "Librería": ["Almacén Libros", "Bodega Papelería", "Depósito General"],
        "Tienda de Electrónicos": ["Almacén Principal", "Bodega Accesorios", "Depósito Reparaciones"],
        "Boutique": ["Almacén Ropa", "Bodega Temporada", "Showroom"],
        "Almacén Mayorista": ["Bodega Principal", "Almacén A", "Almacén B", "Depósito Distribución"],
        "Distribuidora": ["Centro Distribución", "Almacén Norte", "Almacén Sur", "Bodega Central"]
    }
    
    # Tipos de direcciones por ciudad
    address_patterns = {
        "Medellín": ["Carrera {0} #{1}-{2}", "Calle {0} #{1}-{2}", "Transversal {0} #{1}-{2}"],
        "Bogotá": ["Carrera {0} #{1}-{2}", "Calle {0} #{1}-{2}", "Diagonal {0} #{1}-{2}"],
        "Cali": ["Carrera {0} #{1}-{2}", "Calle {0} #{1}-{2}", "Avenida {0} #{1}-{2}"],
        "Barranquilla": ["Carrera {0} #{1}-{2}", "Calle {0} #{1}-{2}", "Vía {0} #{1}-{2}"],
        "Cartagena": ["Carrera {0} #{1}-{2}", "Calle {0} #{1}-{2}", "Avenida {0} #{1}-{2}"],
        "Bucaramanga": ["Carrera {0} #{1}-{2}", "Calle {0} #{1}-{2}", "Transversal {0} #{1}-{2}"],
        "Pereira": ["Carrera {0} #{1}-{2}", "Calle {0} #{1}-{2}", "Avenida {0} #{1}-{2}"],
        "Manizales": ["Carrera {0} #{1}-{2}", "Calle {0} #{1}-{2}", "Transversal {0} #{1}-{2}"]
    }
    
    # Capacidades por tipo de negocio (en m²)
    capacity_ranges = {
        "Supermercado": (200, 800),
        "Farmacia": (50, 200),
        "Ferretería": (150, 500),
        "Librería": (80, 300),
        "Tienda de Electrónicos": (100, 400),
        "Boutique": (60, 250),
        "Almacén Mayorista": (500, 2000),
        "Distribuidora": (800, 3000)
    }
    
    warehouses = []
    warehouse_id = 1
    
    for _, business in businesses_df.iterrows():
        business_type = business['business_type']
        city = business['city']
        business_id = business['id']
        
        # Determinar número de almacenes para este negocio
        min_warehouses, max_warehouses = warehouses_per_business_range
        
        # Negocios más grandes tienen más almacenes
        if business['size'] == 'Grande':
            num_warehouses = random.randint(max_warehouses, max_warehouses + 1)
        elif business['size'] == 'Mediana':
            num_warehouses = random.randint(min_warehouses + 1, max_warehouses)
        else:  # Pequeña
            num_warehouses = random.randint(min_warehouses, min_warehouses + 1)
        
        # Obtener tipos de almacenes disponibles
        available_types = warehouse_types.get(business_type, ["Almacén Principal", "Bodega General"])
        capacity_min, capacity_max = capacity_ranges.get(business_type, (100, 500))
        
        for i in range(num_warehouses):
            # Seleccionar tipo de almacén
            if i < len(available_types):
                warehouse_name = available_types[i]
            else:
                warehouse_name = f"Almacén {i + 1}"
            
            # Generar dirección
            address_formats = address_patterns.get(city, ["Carrera {0} #{1}-{2}"])
            address_format = random.choice(address_formats)
            
            # Números realistas para direcciones colombianas
            carrera_calle = random.randint(1, 80)
            numero1 = random.randint(10, 150)
            numero2 = random.randint(10, 99)
            address = address_format.format(carrera_calle, numero1, numero2)
            
            # Agregar barrio/sector
            barrios = {
                "Medellín": ["El Poblado", "Laureles", "Envigado", "La América", "Robledo"],
                "Bogotá": ["Chapinero", "Zona Rosa", "Suba", "Kennedy", "Fontibón"],
                "Cali": ["El Peñón", "San Fernando", "Granada", "Normandía", "Ciudad Jardín"],
                "Barranquilla": ["El Prado", "Alto Prado", "Villa Country", "Las Flores", "Centro"],
                "Cartagena": ["Bocagrande", "El Laguito", "Manga", "Centro", "Pie de la Popa"],
                "Bucaramanga": ["Cabecera", "Cañaveral", "García Rovira", "Centro", "Provenza"],
                "Pereira": ["El Jardín", "Cuba", "Universidad", "Centro", "Pinares"],
                "Manizales": ["La Sultana", "Versalles", "Palogrande", "Centro", "Milán"]
            }
            
            barrio = random.choice(barrios.get(city, ["Centro", "Norte", "Sur"]))
            full_address = f"{address}, {barrio}, {city}"
            
            # Generar otros datos
            capacity = random.randint(capacity_min, capacity_max)
            
            # Gerentes/responsables ficticios
            managers = [
                "Carlos Rodríguez", "María González", "Juan Pérez", "Ana López",
                "Luis García", "Carmen Martínez", "Roberto Silva", "Patricia Herrera",
                "Miguel Torres", "Lucía Ramírez", "Fernando Castro", "Isabel Moreno"
            ]
            
            # Costo operacional basado en capacidad y ciudad
            cost_per_m2 = {
                "Bogotá": 25000, "Medellín": 22000, "Cali": 20000, "Barranquilla": 18000,
                "Cartagena": 19000, "Bucaramanga": 16000, "Pereira": 15000, "Manizales": 14000
            }
            
            base_cost = cost_per_m2.get(city, 18000)
            operational_cost = capacity * base_cost + random.randint(-500000, 1000000)
            
            warehouse = {
                'id': warehouse_id,
                'name': warehouse_name,
                'address': full_address,
                'business_id': business_id,
                'capacity': capacity,
                'location_type': "Urbano" if random.random() > 0.15 else "Industrial",
                'manager_name': random.choice(managers),
                'operational_cost': operational_cost,
                'created_at': business['created_at'] + timedelta(days=random.randint(1, 90))
            }
            
            warehouses.append(warehouse)
            warehouse_id += 1
    
    return pd.DataFrame(warehouses)

def save_warehouses_csv(df, filename='warehouses.csv'):
    """
    Guarda el DataFrame de almacenes en un archivo CSV
    
    Args:
        df (pandas.DataFrame): DataFrame con datos de almacenes
        filename (str): Nombre del archivo CSV
    """
    filepath = f'../raw/{filename}'
    df.to_csv(filepath, index=False, encoding='utf-8')
    print(f"✅ Archivo {filename} guardado con {len(df)} almacenes")
    print(f"📊 Distribución por tipo de ubicación:")
    print(df['location_type'].value_counts().to_string())
    print(f"\n📊 Almacenes por negocio:")
    print(df['business_id'].value_counts().sort_index().to_string())
    print(f"\n📊 Capacidad promedio por tipo de ubicación:")
    capacity_stats = df.groupby('location_type')['capacity'].agg(['count', 'mean', 'min', 'max']).round(0)
    print(capacity_stats.to_string())

if __name__ == "__main__":
    # Cargar datos de negocios (debe existir)
    try:
        businesses_df = pd.read_csv('../raw/businesses.csv')
        print(f"📋 Cargados {len(businesses_df)} negocios")
    except FileNotFoundError:
        print("❌ Error: Primero debe ejecutar generate_businesses.py")
        exit(1)
    
    # Generar datos
    warehouses_df = generate_warehouses(businesses_df)
    
    # Mostrar preview
    print("\n🏭 PREVIEW DE ALMACENES GENERADOS:")
    print("="*50)
    print(warehouses_df.head(10))
    print(f"\nTotal almacenes: {len(warehouses_df)}")
    
    # Guardar archivo
    save_warehouses_csv(warehouses_df)