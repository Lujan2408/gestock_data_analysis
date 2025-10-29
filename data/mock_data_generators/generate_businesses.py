"""
Generador de datos mockeados para la tabla Businesses de GESTOCK
Crea negocios diversos con diferentes industrias, tamaños y ubicaciones
"""

import pandas as pd
import random
from datetime import datetime, timedelta

def generate_businesses(num_businesses=8):
    """
    Genera datos mockeados para negocios
    
    Args:
        num_businesses (int): Número de negocios a generar
    
    Returns:
        pandas.DataFrame: DataFrame con datos de negocios
    """
    
    # Datos base para generar negocios realistas
    business_types = [
        "Supermercado", "Farmacia", "Ferretería", "Librería", 
        "Tienda de Electrónicos", "Boutique", "Almacén Mayorista", "Distribuidora"
    ]
    
    industries = [
        "Retail", "Farmacéutico", "Construcción", "Educación",
        "Tecnología", "Moda", "Mayorista", "Distribución"
    ]
    
    cities = [
        "Medellín", "Bogotá", "Cali", "Barranquilla", 
        "Cartagena", "Bucaramanga", "Pereira", "Manizales"
    ]
    
    regions = [
        "Antioquia", "Cundinamarca", "Valle del Cauca", "Atlántico",
        "Bolívar", "Santander", "Risaralda", "Caldas"
    ]
    
    company_sizes = ["Pequeña", "Mediana", "Grande"]
    
    # Generar datos
    businesses = []
    start_date = datetime(2023, 1, 1)
    
    for i in range(num_businesses):
        # Seleccionar tipo y datos relacionados
        business_type = business_types[i] if i < len(business_types) else random.choice(business_types)
        industry = industries[i] if i < len(industries) else random.choice(industries)
        city = cities[i] if i < len(cities) else random.choice(cities)
        region = regions[i] if i < len(regions) else random.choice(regions)
        
        # Generar nombre de empresa
        if business_type == "Supermercado":
            names = ["MercaFresh", "SuperCompras", "AlimentosMás", "FreshMarket"]
        elif business_type == "Farmacia":
            names = ["FarmaVida", "SaludPlus", "MediCare", "FarmaBienestar"]
        elif business_type == "Ferretería":
            names = ["FerreTotal", "ConstruMax", "HerramientasPlus", "FerreHogar"]
        elif business_type == "Librería":
            names = ["LibrosMundo", "PapeleríaTotal", "EducaLibros", "LeeríaMás"]
        elif business_type == "Tienda de Electrónicos":
            names = ["TechnoStore", "ElectroMax", "DigitalWorld", "TecnologíaPlus"]
        elif business_type == "Boutique":
            names = ["ModaChic", "EstiloUnico", "TrendyFashion", "BellaRopa"]
        else:
            names = ["ComercialTotal", "DistribuMax", "MayoristaPlus", "SuministrosGenerales"]
        
        company_name = f"{random.choice(names)} {city}"
        
        # Datos del negocio
        business = {
            'id': i + 1,
            'name': company_name,
            'industry': industry,
            'business_type': business_type,
            'size': random.choice(company_sizes),
            'city': city,
            'region': region,
            'created_at': start_date + timedelta(days=random.randint(0, 600))
        }
        
        businesses.append(business)
    
    return pd.DataFrame(businesses)

def save_businesses_csv(df, filename='businesses.csv'):
    """
    Guarda el DataFrame de negocios en un archivo CSV
    
    Args:
        df (pandas.DataFrame): DataFrame con datos de negocios
        filename (str): Nombre del archivo CSV
    """
    filepath = f'../raw/{filename}'
    df.to_csv(filepath, index=False, encoding='utf-8')
    print(f"✅ Archivo {filename} guardado con {len(df)} negocios")
    print(f"📊 Distribución por industria:")
    print(df['industry'].value_counts().to_string())
    print(f"\n📊 Distribución por tamaño:")
    print(df['size'].value_counts().to_string())

if __name__ == "__main__":
    # Generar datos
    businesses_df = generate_businesses(8)
    
    # Mostrar preview
    print("🏢 PREVIEW DE NEGOCIOS GENERADOS:")
    print("="*50)
    print(businesses_df.head())
    print(f"\nTotal negocios: {len(businesses_df)}")
    
    # Guardar archivo
    save_businesses_csv(businesses_df)