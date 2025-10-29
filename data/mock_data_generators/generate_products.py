"""
Generador de datos mockeados para la tabla Products de GESTOCK
Crea productos diversos con categorías, precios realistas y márgenes variables
"""

import pandas as pd
import random
from datetime import datetime, timedelta

def generate_products(num_products=85):
    """
    Genera datos mockeados para productos
    
    Args:
        num_products (int): Número de productos a generar
    
    Returns:
        pandas.DataFrame: DataFrame con datos de productos
    """
    
    # Categorías de productos con datos específicos
    product_categories = {
        "Electrónicos": {
            "products": [
                "Smartphone Samsung", "iPhone", "Laptop HP", "Laptop Dell", "Tablet Android",
                "Smart TV 43\"", "Smart TV 55\"", "Auriculares Bluetooth", "Cargador Universal",
                "Mouse Inalámbrico", "Teclado Mecánico", "Monitor 24\"", "Parlante Bluetooth",
                "Cámara Digital", "Consola Gaming"
            ],
            "price_range": (150000, 3500000),
            "cost_margin": (0.6, 0.8),  # Costo es 60-80% del precio
            "suppliers": ["TechDistributor", "ElectroImport", "DigitalSupply", "TechWorld"]
        },
        "Ropa": {
            "products": [
                "Camiseta Polo", "Jean Clásico", "Vestido Casual", "Chaqueta Deportiva",
                "Zapatos Casuales", "Zapatillas Deportivas", "Camisa Formal", "Pantalón Formal",
                "Blusa Mujer", "Sudadera", "Short Deportivo", "Falda", "Bufanda", "Gorra"
            ],
            "price_range": (25000, 350000),
            "cost_margin": (0.4, 0.6),
            "suppliers": ["ModaImport", "TextilSupply", "FashionDist", "RopaTotal"]
        },
        "Alimentos": {
            "products": [
                "Arroz Premium 1kg", "Aceite Vegetal 1L", "Azúcar Blanca 1kg", "Sal Marina 500g",
                "Pasta Integral 500g", "Cereal Granola", "Leche Entera 1L", "Yogurt Natural",
                "Pan Integral", "Galletas Avena", "Café Premium 250g", "Té Verde", "Miel Natural"
            ],
            "price_range": (3500, 45000),
            "cost_margin": (0.7, 0.85),
            "suppliers": ["AlimentosDist", "NutriSupply", "FoodImport", "AgriDistributor"]
        },
        "Hogar": {
            "products": [
                "Detergente Líquido 1L", "Jabón en Barra", "Papel Higiénico 12u", "Servilletas",
                "Ambientador", "Limpiador Multiusos", "Escoba", "Trapero", "Balde Plástico",
                "Toalla Baño", "Sábanas Queen", "Almohada Memory", "Cortina Baño"
            ],
            "price_range": (8000, 120000),
            "cost_margin": (0.5, 0.7),
            "suppliers": ["HogarSupply", "CleanDistributor", "HomeImport", "DomesticSupply"]
        },
        "Salud": {
            "products": [
                "Acetaminofén 500mg", "Ibuprofeno 400mg", "Vitamina C", "Alcohol Antiséptico",
                "Vendas Elásticas", "Termómetro Digital", "Mascarillas N95", "Gel Antibacterial",
                "Protector Solar SPF50", "Shampoo Anticaspa", "Crema Hidratante", "Suero Oral"
            ],
            "price_range": (12000, 85000),
            "cost_margin": (0.6, 0.75),
            "suppliers": ["FarmaDistributor", "HealthSupply", "MediImport", "SaludTotal"]
        },
        "Construcción": {
            "products": [
                "Cemento Gris 50kg", "Arena Fina m³", "Grava m³", "Ladrillo Común u100",
                "Varilla 12mm 6m", "Alambre Galvanizado", "Clavos 2\" 1kg", "Tornillos Varios",
                "Pintura Blanca 1gal", "Brocha 4\"", "Rodillo", "Tubo PVC 4\" 6m", "Llave Agua"
            ],
            "price_range": (15000, 280000),
            "cost_margin": (0.65, 0.8),
            "suppliers": ["ConstruMax", "MaterialesPro", "FerreDistribuidor", "BuildSupply"]
        },
        "Oficina": {
            "products": [
                "Papel Bond A4 500h", "Bolígrafos Azul 12u", "Lápices HB 12u", "Marcadores",
                "Carpetas Manila", "Archivador AZ", "Calculadora Básica", "Grapadora",
                "Perforadora", "Pegamento", "Cinta Adhesiva", "Clips Metálicos", "Post-it"
            ],
            "price_range": (2500, 65000),
            "cost_margin": (0.5, 0.65),
            "suppliers": ["OfficeSupply", "PapeleríaDist", "EducaImport", "OfficeMax"]
        }
    }
    
    products = []
    product_id = 1
    start_date = datetime(2022, 6, 1)
    
    # Distribuir productos por categoría
    products_per_category = num_products // len(product_categories)
    remaining_products = num_products % len(product_categories)
    
    for category, category_data in product_categories.items():
        # Número de productos para esta categoría
        category_count = products_per_category
        if remaining_products > 0:
            category_count += 1
            remaining_products -= 1
        
        available_products = category_data["products"]
        price_min, price_max = category_data["price_range"]
        cost_min, cost_max = category_data["cost_margin"]
        suppliers = category_data["suppliers"]
        
        for i in range(category_count):
            # Seleccionar producto (repetir si es necesario)
            product_base = available_products[i % len(available_products)]
            
            # Agregar variaciones si hay repetición
            if i >= len(available_products):
                variations = ["Premium", "Económico", "Deluxe", "Básico", "Pro"]
                product_name = f"{product_base} {random.choice(variations)}"
            else:
                product_name = product_base
            
            # Generar precio y costo
            price = random.randint(price_min, price_max)
            cost_margin = random.uniform(cost_min, cost_max)
            cost_price = round(price * cost_margin)
            profit_margin = round(((price - cost_price) / price) * 100, 1)
            
            product = {
                'id': product_id,
                'name': product_name,
                'category': category,
                'price': price,
                'cost_price': cost_price,
                'profit_margin': profit_margin,
                'supplier': random.choice(suppliers),
                'description': f"{product_name} - {category}",
                'created_at': start_date + timedelta(days=random.randint(0, 500))
            }
            
            products.append(product)
            product_id += 1
    
    return pd.DataFrame(products)

def save_products_csv(df, filename='products.csv'):
    """
    Guarda el DataFrame de productos en un archivo CSV
    
    Args:
        df (pandas.DataFrame): DataFrame con datos de productos
        filename (str): Nombre del archivo CSV
    """
    filepath = f'../raw/{filename}'
    df.to_csv(filepath, index=False, encoding='utf-8')
    print(f"✅ Archivo {filename} guardado con {len(df)} productos")
    print(f"📊 Distribución por categoría:")
    print(df['category'].value_counts().to_string())
    print(f"\n💰 Rango de precios por categoría:")
    price_stats = df.groupby('category')['price'].agg(['min', 'max', 'mean']).round(0)
    print(price_stats.to_string())

if __name__ == "__main__":
    # Generar datos
    products_df = generate_products(85)
    
    # Mostrar preview
    print("📦 PREVIEW DE PRODUCTOS GENERADOS:")
    print("="*50)
    print(products_df.head(10))
    print(f"\nTotal productos: {len(products_df)}")
    
    # Guardar archivo
    save_products_csv(products_df)