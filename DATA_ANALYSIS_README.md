# 📊 GESTOCK - Análisis de Datos e Inteligencia de Negocio

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green?style=for-the-badge&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-orange?style=for-the-badge&logo=plotly)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-yellow?style=for-the-badge)

**Sistema de análisis de datos para optimización de inventarios**

[Características](#-características-principales) • [Instalación](#-instalación) • [Datos Generados](#-datos-generados) • [Estructura](#-estructura-del-proyecto)

</div>

---

## 📋 Tabla de Contenidos

- [Resumen Ejecutivo](#-resumen-ejecutivo)
- [Introducción](#-introducción)
- [Propósito del Software](#-propósito-del-software)
- [Problemas a Resolver](#-problemas-a-resolver)
- [Solución Propuesta](#-solución-propuesta)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Datos Generados](#-datos-generados)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Roadmap](#-roadmap)

---

## 🎯 Resumen Ejecutivo

### Descripción del Proyecto
**GESTOCK Data Analytics** es un sistema de análisis de datos desarrollado como complemento del sistema de gestión de inventario GESTOCK. El proyecto se enfoca en transformar datos transaccionales en insights estratégicos mediante técnicas de análisis de datos, visualización y modelado predictivo básico.

### Objetivos Principales
- ✅ **Análisis Exploratorio**: Identificar patrones en datos de inventario multi-tenant
- ✅ **Visualización Interactiva**: Crear dashboards para toma de decisiones
- 🔄 **Análisis Predictivo**: Desarrollar modelos básicos de predicción de demanda
- 🔄 **Optimización**: Generar recomendaciones para gestión eficiente de inventarios

### Resultados Esperados
- **15-20% reducción** en costos de inventario mediante optimización
- **Mejora significativa** en toma de decisiones basada en datos
- **Identificación proactiva** de productos problemáticos y oportunidades
- **Sistema escalable** para múltiples tipos de negocio

---

## 🌟 Introducción

### Contexto del Proyecto
Este proyecto surge como una extensión del sistema **GESTOCK** - un sistema de gestión de inventario multi-tenant desarrollado con Spring Boot. Mientras GESTOCK maneja las operaciones transaccionales, este módulo de análisis convierte esos datos en inteligencia de negocio accionable.

### Justificación
Los negocios modernos generan grandes volúmenes de datos transaccionales, pero carecen de herramientas para extraer insights valiosos. Este proyecto llena ese vacío proporcionando:

- **Análisis automatizado** de patrones de inventario
- **Visualizaciones intuitivas** para gerentes y analistas
- **Alertas tempranas** sobre problemas de stock
- **Benchmarking** entre diferentes tipos de negocio

### Alcance General
- **Análisis histórico**: 6 meses de datos transaccionales simulados
- **Multi-tenant**: Análisis comparativo entre 8 tipos de negocio
- **Tiempo real simulado**: Datos con patrones estacionales y temporales realistas
- **Escalabilidad**: Arquitectura preparada para datos reales

### Repositorio GitHub
**🔗 [github.com/Lujan2408/gestock_data_analysis](https://github.com/Lujan2408/gestock_data_analysis)**

---

## 🎪 Propósito del Software

### Objetivo del Desarrollo
Transformar datos crudos de inventario en inteligencia de negocio accionable, proporcionando a los stakeholders herramientas para optimizar operaciones y aumentar rentabilidad.

### Público Objetivo

#### 👨‍💼 **Gerentes de Operaciones**
- Dashboards ejecutivos con KPIs clave
- Reportes de rendimiento por almacén
- Análisis comparativo de eficiencia

#### 📊 **Analistas de Inventario**
- Herramientas de análisis detallado
- Identificación de patrones y anomalías
- Modelos predictivos de demanda

#### 🏪 **Propietarios de PYMES**
- Insights simples y accionables
- Recomendaciones de reabastecimiento
- Análisis de rentabilidad por producto

#### 🏭 **Administradores de Almacén**
- Alertas de stock crítico
- Optimización de ubicaciones
- Análisis de rotación de productos

### Impacto Esperado
- **Optimización de inventarios**: Reducción de costos de almacenamiento
- **Mejora en cash flow**: Menos capital inmovilizado en stock muerto
- **Incremento en ventas**: Mejor disponibilidad de productos estrella
- **Decisiones data-driven**: Reemplazo de intuición por análisis objetivo

---

## 🔧 Problemas a Resolver

### Situación Actual
Los negocios que utilizan GESTOCK enfrentan varios desafíos en la gestión de datos:

#### 📈 **Falta de Visibilidad**
- Datos dispersos sin análisis centralizado
- Ausencia de métricas clave de rendimiento
- Dificultad para identificar tendencias

#### 🎯 **Decisiones Subóptimas**
- Compras basadas en intuición, no en datos
- Falta de alertas tempranas sobre problemas
- Ausencia de benchmarking entre ubicaciones

#### 💰 **Ineficiencias Operativas**
- Stock muerto que inmoviliza capital
- Roturas de stock en productos críticos
- Costos elevados de almacenamiento

#### 📊 **Carencia de Insights Comparativos**
- Imposibilidad de comparar rendimiento entre negocios
- Falta de mejores prácticas identificadas
- Ausencia de análisis predictivo

### Necesidades Detectadas

1. **Análisis de Tendencias**: Identificar patrones estacionales y temporales
2. **Predicción de Demanda**: Anticipar necesidades de reabastecimiento
3. **Optimización de Stock**: Balancear disponibilidad vs costos
4. **Benchmarking**: Comparar rendimiento entre unidades de negocio
5. **Alertas Inteligentes**: Notificaciones proactivas sobre anomalías

---

## 💡 Solución Propuesta

### Descripción de la Solución
**GESTOCK Data Analytics** proporciona una suite completa de herramientas de análisis que incluye:

#### 🔍 **Análisis Exploratorio Automatizado**
- Perfilado automático de datos transaccionales
- Identificación de patrones y anomalías
- Estadísticas descriptivas por dimensión de negocio

#### 📊 **Visualizaciones Interactivas**
- Dashboards ejecutivos con KPIs principales
- Gráficos de tendencias temporales
- Análisis comparativo multi-dimensional

#### 🤖 **Modelos Predictivos Básicos**
- Predicción de demanda por producto
- Identificación de productos en riesgo
- Recomendaciones de reabastecimiento

#### 📋 **Reportes Personalizados**
- Reportes automatizados por tipo de negocio
- Alertas configurables por usuario
- Exportación en múltiples formatos

### Beneficios

#### 💰 **Financieros**
- **15-20% reducción** en costos de inventario
- **Mejora en ROI** por optimización de compras
- **Liberación de capital** por reducción de stock muerto

#### 📈 **Operacionales**
- **Mejor planificación** de compras y reposición
- **Reducción de roturas** de stock crítico
- **Optimización de espacio** de almacenamiento

#### 🎯 **Estratégicos**
- **Insights competitivos** entre tipos de negocio
- **Identificación de oportunidades** de crecimiento
- **Base sólida** para decisiones de expansión

### Innovación

#### 🏢 **Análisis Multi-Tenant Comparativo**
- Primera solución que permite benchmarking entre diferentes tipos de negocio
- Identificación de mejores prácticas transferibles

#### 🔄 **Integración Seamless**
- Diseñado específicamente para datos de GESTOCK
- Sin necesidad de ETL complejos o transformaciones manuales

#### 📊 **Visualizaciones Adaptativas**
- Dashboards que se adaptan automáticamente al tipo de negocio
- Métricas relevantes según la industria específica

---

## 🛠️ Tecnologías Utilizadas

### Stack Principal

#### 🐍 **Python 3.11+**
- Lenguaje principal para análisis de datos
- Ecosistema maduro y extenso de librerías

#### 📊 **Pandas 2.0+**
- Manipulación y análisis de datos estructurados
- Operaciones eficientes en DataFrames
- Integración nativa con otras librerías

#### 📈 **Matplotlib & Seaborn**
- Generación de visualizaciones estáticas
- Gráficos publication-ready
- Amplia personalización visual

#### 🔢 **NumPy**
- Computación numérica eficiente
- Base para operaciones matemáticas complejas

### Herramientas de Desarrollo

#### 📓 **Jupyter Notebooks**
- Desarrollo iterativo y experimentación
- Documentación integrada con código
- Ideal para análisis exploratorio

#### 📦 **UV Package Manager**
- Gestión moderna de dependencias Python
- Instalación rápida y resolución eficiente
- Entornos virtuales integrados

#### 🔧 **VS Code**
- IDE principal con extensiones Python
- Integración con Git y Jupyter
- Debugging avanzado

### Plataformas y Servicios

#### 🐙 **GitHub**
- Control de versiones distribuido
- Colaboración y revisión de código
- Gestión de issues y releases

#### 🖥️ **Desarrollo Local**
- Entorno completamente local para desarrollo
- Sin dependencias de servicios cloud
- Fácil reproducibilidad

---

## 📊 Datos Generados

### Resumen de Datasets

Nuestro sistema ha generado exitosamente **datasets realistas** que simulan 6 meses de operación de múltiples negocios:

#### 🏢 **Negocios (businesses.csv)**
- **8 negocios** en diferentes ciudades colombianas
- **Industrias diversas**: Retail, Farmacéutico, Construcción, Tecnología
- **Tamaños variados**: Pequeña (3), Mediana (3), Grande (2)
- **Ubicaciones**: Medellín, Bogotá, Cali, Barranquilla, etc.

#### 📦 **Productos (products.csv)**
- **85 productos** en 7 categorías principales
- **Categorías**: Electrónicos, Ropa, Alimentos, Hogar, Salud, Construcción, Oficina
- **Precios realistas**: Desde $2,500 hasta $3,500,000
- **Márgenes variables**: 15% - 60% según categoría

#### 🏭 **Almacenes (warehouses.csv)**
- **23 almacenes** distribuidos entre negocios
- **2-4 almacenes** por negocio según tamaño
- **Direcciones reales** en ciudades colombianas  
- **Capacidades**: 50m² - 3,000m² según tipo de negocio

#### 👥 **Usuarios (users.csv)**
- **31 usuarios** distribuidos entre negocios
- **Roles**: 30% ADMIN, 70% USER
- **95% usuarios activos** con actividad reciente
- **Emails únicos** y datos colombianos realistas

#### 📊 **Stock (warehouse_products.csv)**
- **547 registros** de stock activo
- **Stock inteligente** por tipo de negocio y categoría
- **Probabilidades específicas** de asignación producto-almacén
- **Stock mín/máx** configurado por industria

#### 💱 **Transacciones (transactions.csv)**
- **1,870 transacciones** en 6 meses de histórico
- **Patrones estacionales** por categoría de producto
- **Actividad reducida** fines de semana (realista)
- **60% SALIDAS, 40% ENTRADAS** (ratio comercial típico)

### Estadísticas Clave

#### 💰 **Valor Total de Inventario**
- **~$85,000,000** en valor total de stock
- **Rango por negocio**: $3M - $25M según tamaño
- **Distribución equilibrada** entre categorías

#### 📈 **Volumen Transaccional**
- **142,891 unidades** ingresadas (ENTRADAS)
- **98,234 unidades** vendidas (SALIDAS)  
- **44,657 unidades** de balance neto positivo
- **Rotación promedio**: 2.1x en 6 meses

#### 🏆 **Distribución de Actividad**
- **Supermercados/Distribuidoras**: 45% de transacciones
- **Farmacias**: 20% de transacciones
- **Ferreterías**: 15% de transacciones
- **Otros**: 20% de transacciones

### Patrones Realistas Implementados

#### 📅 **Estacionalidad**
- **Construcción**: Pico enero-abril (temporada seca)
- **Ropa**: Picos marzo (regreso escolar) y diciembre (navidad)
- **Electrónicos**: Incremento noviembre-diciembre (Black Friday/Navidad)
- **Alimentos**: Actividad constante con pico diciembre

#### 📊 **Patrones Semanales**
- **Lunes-Viernes**: Actividad normal (100%)
- **Sábados**: Reducción 20% (80% actividad)
- **Domingos**: Reducción 50% (50% actividad)

#### 🎯 **Lógica de Negocio**
- **Stock bajo** → Mayor probabilidad de ENTRADAS (80%)
- **Stock alto** → Mayor probabilidad de SALIDAS (70%)
- **Usuarios operan solo** en almacenes de su negocio
- **Stock nunca negativo** (validación automática)

---

## 🏗️ Estructura del Proyecto

```
analisis_datos_GESTOCK/
├── 📁 data/
│   ├── 📁 raw/                         # Datos generados (CSV)
│   │   ├── businesses.csv              # 8 negocios
│   │   ├── products.csv                # 85 produtos
│   │   ├── warehouses.csv              # 23 almacenes
│   │   ├── users.csv                   # 31 usuarios
│   │   ├── warehouse_products.csv      # 547 registros stock
│   │   └── transactions.csv            # 1,870 transacciones
│   │
│   ├── 📁 processed/                   # Datos procesados (futuro)
│   └── 📁 mock_data_generators/        # Scripts generadores
│       ├── generate_businesses.py      # Generador negocios
│       ├── generate_products.py        # Generador productos
│       ├── generate_warehouses.py      # Generador almacenes
│       ├── generate_users.py           # Generador usuarios
│       ├── generate_warehouse_products.py # Generador stock
│       ├── generate_transactions.py    # Generador transacciones
│       ├── generate_base_data.py       # Script maestro base
│       └── generate_transactional_data.py # Script maestro transaccional
│
├── 📁 notebooks/                       # Análisis Jupyter (próximo)
│   ├── 01_exploratory_analysis.ipynb   # Análisis exploratorio
│   ├── 02_inventory_analysis.ipynb     # Análisis inventario
│   ├── 03_business_insights.ipynb      # Insights de negocio
│   └── 04_predictive_analysis.ipynb    # Análisis predictivo
│
├── 📁 src/                            # Código reutilizable (próximo)
│   ├── __init__.py
│   ├── data_processing.py             # Funciones procesamiento
│   ├── visualization.py               # Funciones visualización
│   └── analysis_functions.py          # Funciones análisis
│
├── 📁 reports/                        # Reportes generados (próximo)
│   ├── 📁 images/                     # Gráficos exportados
│   └── 📁 html/                       # Reportes HTML
│
├── pyproject.toml                     # Configuración UV
├── README.md                          # Documentación GESTOCK original
└── DATA_ANALYSIS_README.md            # Este documento
```

---

## ⚙️ Instalación

### Prerrequisitos

- **Python 3.11+** instalado
- **UV package manager** instalado
- **Git** para clonar el repositorio

### Pasos de Instalación

#### 1. Clonar el Repositorio

```bash
git clone https://github.com/Lujan2408/gestock_data_analysis.git
cd gestock_data_analysis
```

#### 2. Crear Entorno Virtual con UV

```bash
# UV creará automáticamente el entorno virtual
uv sync
```

#### 3. Activar Entorno Virtual

```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

#### 4. Verificar Instalación

```bash
uv pip list
```

Deberías ver instaladas las dependencias:
- pandas
- matplotlib  
- seaborn
- numpy

---

## 🚀 Uso

### Generar Datos Mock

#### Opción 1: Generar Todos los Datos
```bash
cd data/mock_data_generators
python generate_base_data.py
python generate_transactional_data.py
```

#### Opción 2: Generar por Módulos
```bash
cd data/mock_data_generators

# Datos base
python generate_businesses.py
python generate_products.py  
python generate_warehouses.py

# Datos transaccionales
python generate_users.py
python generate_warehouse_products.py
python generate_transactions.py
```

### Verificar Datos Generados

```bash
# Verificar archivos generados
ls -la data/raw/

# Ver estadísticas rápidas
python -c "
import pandas as pd
print('Businesses:', len(pd.read_csv('data/raw/businesses.csv')))
print('Products:', len(pd.read_csv('data/raw/products.csv'))) 
print('Warehouses:', len(pd.read_csv('data/raw/warehouses.csv')))
print('Users:', len(pd.read_csv('data/raw/users.csv')))
print('Stock records:', len(pd.read_csv('data/raw/warehouse_products.csv')))
print('Transactions:', len(pd.read_csv('data/raw/transactions.csv')))
"
```

### Explorar Datos (Próximamente)

```bash
# Iniciar Jupyter para análisis
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```

---

## 🗺️ Roadmap

### ✅ **Fase 1: Configuración y Datos Base** (Completada)
- [x] Estructura del proyecto
- [x] Generación de negocios, productos y almacenes
- [x] Validación de integridad de datos

### ✅ **Fase 2: Datos Transaccionales** (Completada)  
- [x] Generación de usuarios y stock inicial
- [x] Transacciones con patrones realistas
- [x] Validación de reglas de negocio

### 🔄 **Fase 3: Análisis Exploratorio** (En Desarrollo)
- [ ] Notebook de análisis exploratorio
- [ ] Estadísticas descriptivas avanzadas
- [ ] Identificación de patrones iniciales

### 📅 **Fase 4: Análisis de Inventario** (Próximo)
- [ ] Métricas de rotación de inventario
- [ ] Análisis de productos estrella vs problemáticos
- [ ] Identificación de stock crítico

### 📅 **Fase 5: Insights de Negocio** (Próximo)
- [ ] Análisis comparativo multi-tenant
- [ ] Benchmarking por industria
- [ ] Identificación de mejores prácticas

### 📅 **Fase 6: Análisis Predictivo** (Próximo)
- [ ] Modelos básicos de predicción de demanda
- [ ] Recomendaciones de reabastecimiento
- [ ] Alertas inteligentes

### 📅 **Fase 7: Documentación Final** (Próximo)
- [ ] Módulos de análisis reutilizables
- [ ] Documentación técnica completa
- [ ] Presentación de resultados

---

## 📞 Información del Proyecto

### 👥 Equipo de Desarrollo
- **Desarrollador Principal**: Lujan2408
- **Institución**: CESDE - Nuevas Tecnologías
- **Tipo**: Proyecto Integrador

### 📅 Timeline
- **Inicio**: Octubre 2025
- **Duración Estimada**: 8 semanas
- **Estado Actual**: Fase 3 - Análisis Exploratorio

### 🔗 Enlaces
- **Repositorio**: [github.com/Lujan2408/gestock_data_analysis](https://github.com/Lujan2408/gestock_data_analysis)
- **GESTOCK Backend**: Sistema base de gestión de inventario
- **Documentación Técnica**: Ver README.md principal

---

## 📄 Licencia

Este proyecto es desarrollado como **Proyecto Académico** para CESDE - Nuevas Tecnologías.

---

<div align="center">

**⭐ Proyecto en desarrollo activo - Octubre 2025 ⭐**

Desarrollado con ❤️ para optimizar la gestión de inventarios mediante análisis de datos

</div>