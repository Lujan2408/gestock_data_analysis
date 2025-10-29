"""
Generador de datos mockeados para la tabla Users de GESTOCK
Crea usuarios distribuidos entre negocios con roles y datos realistas
"""

import pandas as pd
import random
from datetime import datetime, timedelta

def generate_users(businesses_df, users_per_business_range=(2, 5)):
    """
    Genera datos mockeados para usuarios basados en los negocios existentes
    
    Args:
        businesses_df (pandas.DataFrame): DataFrame con datos de negocios
        users_per_business_range (tuple): Rango de usuarios por negocio
    
    Returns:
        pandas.DataFrame: DataFrame con datos de usuarios
    """
    
    # Nombres y apellidos realistas
    first_names = [
        "Carlos", "María", "Juan", "Ana", "Luis", "Carmen", "Roberto", "Patricia",
        "Miguel", "Lucía", "Fernando", "Isabel", "Diego", "Claudia", "Andrés",
        "Mónica", "Javier", "Diana", "Ricardo", "Alejandra", "Sergio", "Natalia",
        "Óscar", "Paola", "Mauricio", "Adriana", "Gonzalo", "Cristina", "Raúl",
        "Valeria", "Esteban", "Marcela", "Tomás", "Sandra", "Nicolás", "Lorena"
    ]
    
    last_names = [
        "García", "Rodríguez", "López", "Martínez", "González", "Pérez", "Sánchez",
        "Ramírez", "Torres", "Flores", "Rivera", "Gómez", "Díaz", "Vargas",
        "Castillo", "Herrera", "Mendoza", "Morales", "Jiménez", "Ruiz", "Hernández",
        "Medina", "Castro", "Ortiz", "Ramos", "Delgado", "Aguilar", "Guerrero",
        "Vega", "Romero", "Álvarez", "Muñoz", "Moreno", "Silva", "Gutiérrez"
    ]
    
    # Dominios de email por ciudad/región
    email_domains = [
        "gmail.com", "hotmail.com", "yahoo.com", "outlook.com", "correo.com",
        "empresarial.com", "negocio.co", "corporativo.com"
    ]
    
    # Roles según tipo de negocio
    role_distribution = {
        "ADMIN": 0.3,  # 30% administradores
        "USER": 0.7    # 70% usuarios regulares
    }
    
    users = []
    user_id = 1
    
    for _, business in businesses_df.iterrows():
        business_id = business['id']
        business_size = business['size']
        business_name = business['name']
        
        # Determinar número de usuarios por negocio
        min_users, max_users = users_per_business_range
        
        if business_size == 'Grande':
            num_users = random.randint(max_users, max_users + 2)
        elif business_size == 'Mediana':
            num_users = random.randint(min_users + 1, max_users)
        else:  # Pequeña
            num_users = random.randint(min_users, min_users + 1)
        
        # Asegurar al menos 1 ADMIN por negocio
        roles = ['ADMIN']
        remaining_users = num_users - 1
        
        # Distribuir roles restantes
        for _ in range(remaining_users):
            if random.random() < role_distribution['ADMIN']:
                roles.append('ADMIN')
            else:
                roles.append('USER')
        
        # Generar usuarios
        used_emails = set()
        
        for i in range(num_users):
            # Generar nombre completo
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            full_name = f"{first_name} {last_name}"
            
            # Generar email único
            base_email = f"{first_name.lower()}.{last_name.lower()}"
            domain = random.choice(email_domains)
            email = f"{base_email}@{domain}"
            
            # Si el email ya existe, agregar número
            counter = 1
            while email in used_emails:
                email = f"{base_email}{counter}@{domain}"
                counter += 1
            
            used_emails.add(email)
            
            # Asignar rol
            role = roles[i] if i < len(roles) else 'USER'
            
            # Fecha de creación (después del negocio)
            business_created = pd.to_datetime(business['created_at'])
            days_after_business = random.randint(1, 120)  # 1-4 meses después
            created_at = business_created + timedelta(days=days_after_business)
            
            # Generar contraseña hasheada ficticia (simulando BCrypt)
            # En realidad sería hasheada, pero para datos mock usamos un patrón
            password_hash = f"$2a$10${''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./', k=53))}"
            
            # Estado del usuario
            is_active = True if random.random() > 0.05 else False  # 95% activos
            
            # Datos adicionales
            phone_number = f"3{random.randint(10, 99)}{random.randint(1000000, 9999999)}"
            
            user = {
                'id': user_id,
                'email': email,
                'password_hash': password_hash,
                'full_name': full_name,
                'first_name': first_name,
                'last_name': last_name,
                'business_id': business_id,
                'role': role,
                'is_active': is_active,
                'phone_number': phone_number,
                'created_at': created_at,
                'last_login': created_at + timedelta(days=random.randint(0, 30)) if is_active else None
            }
            
            users.append(user)
            user_id += 1
    
    return pd.DataFrame(users)

def save_users_csv(df, filename='users.csv'):
    """
    Guarda el DataFrame de usuarios en un archivo CSV
    
    Args:
        df (pandas.DataFrame): DataFrame con datos de usuarios
        filename (str): Nombre del archivo CSV
    """
    filepath = f'../raw/{filename}'
    df.to_csv(filepath, index=False, encoding='utf-8')
    print(f"✅ Archivo {filename} guardado con {len(df)} usuarios")
    print(f"📊 Distribución por rol:")
    print(df['role'].value_counts().to_string())
    print(f"\n📊 Usuarios por negocio:")
    users_per_business = df['business_id'].value_counts().sort_index()
    print(users_per_business.to_string())
    print(f"\n📊 Usuarios activos: {df['is_active'].sum()}/{len(df)} ({(df['is_active'].sum()/len(df)*100):.1f}%)")

if __name__ == "__main__":
    # Cargar datos de negocios
    try:
        businesses_df = pd.read_csv('../raw/businesses.csv')
        print(f"📋 Cargados {len(businesses_df)} negocios")
    except FileNotFoundError:
        print("❌ Error: Primero debe ejecutar generate_base_data.py")
        exit(1)
    
    # Generar datos
    users_df = generate_users(businesses_df)
    
    # Mostrar preview
    print("\n👥 PREVIEW DE USUARIOS GENERADOS:")
    print("="*50)
    print(users_df[['email', 'full_name', 'business_id', 'role', 'is_active']].head(10))
    print(f"\nTotal usuarios: {len(users_df)}")
    
    # Guardar archivo
    save_users_csv(users_df)