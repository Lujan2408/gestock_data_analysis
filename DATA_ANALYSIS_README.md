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
- **27 almacenes** distribuidos entre negocios
- **2-4 almacenes** por negocio según tamaño
- **Direcciones reales** en ciudades colombianas  
- **Capacidades**: 50m² - 3,000m² según tipo de negocio

#### 👥 **Usuarios (users.csv)**
- **32 usuarios** distribuidos entre negocios
- **Roles**: 30% ADMIN, 70% USER
- **95% usuarios activos** con actividad reciente
- **Emails únicos** y datos colombianos realistas

#### 📊 **Stock (warehouse_products.csv)**
- **1,207 registros** de stock activo
- **Stock inteligente** por tipo de negocio y categoría
- **Probabilidades específicas** de asignación producto-almacén
- **Stock mín/máx** configurado por industria

#### 💱 **Transacciones (transactions.csv)**
- **1,900 transacciones** en 6 meses de histórico
- **Patrones estacionales** por categoría de producto
- **Actividad reducida** fines de semana (realista)
- **62% SALIDAS, 38% ENTRADAS** (ratio comercial típico)

### Estadísticas Clave

#### 💰 **Valor Total de Inventario**
- **$99,981,593,968** (~$100 mil millones) en valor total de stock
- **Rango por negocio**: Desde $3M hasta $25M según tamaño
- **Distribución equilibrada** entre categorías con concentración en Electrónicos

#### 📈 **Volumen Transaccional**
- **1,900 transacciones** totales procesadas
- **392,520 unidades** en stock total actual
- **62% SALIDAS vs 38% ENTRADAS** (flujo comercial típico)
- **Hora pico**: 9:00 AM con mayor actividad
- **Día más activo**: Jueves con mayor volumen

#### 🏆 **Distribución de Actividad**
- **Distribuidoras**: Tipo de negocio más activo
- **Construcción**: Industria más común y más estacional
- **Electrónicos**: Categoría de mayor valor en inventario
- **Jueves 9:00 AM**: Momento de mayor actividad transaccional

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
│   │   ├── warehouses.csv              # 27 almacenes
│   │   ├── users.csv                   # 32 usuarios
│   │   ├── warehouse_products.csv      # 1,207 registros stock
│   │   └── transactions.csv            # 1,900 transacciones
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

#### 2. Instalar Dependencias con UV

```bash
# UV creará automáticamente el entorno virtual
uv sync

# Si no tienes UV instalado, usa pip:
pip install pandas matplotlib seaborn numpy jupyter
```

#### 3. Verificar Instalación

```bash
uv pip list
```

**Dependencias principales instaladas:**
- ✅ **pandas**: Manipulación de datos
- ✅ **matplotlib**: Visualizaciones básicas  
- ✅ **seaborn**: Visualizaciones estadísticas
- ✅ **numpy**: Computación numérica
- ✅ **jupyter**: Notebooks interactivos

#### 4. Verificar Estructura de Archivos

```bash
# Verificar que los datos estén generados
ls data/raw/
# Debe mostrar: businesses.csv, products.csv, warehouses.csv, users.csv, warehouse_products.csv, transactions.csv
```

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

### Explorar Análisis Completado

#### Opción 1: Ver Notebook Ejecutado
```bash
# Abrir el notebook con todos los resultados
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```

#### Opción 2: Ver Métricas Exportadas
```bash
# Ver métricas clave del análisis
python -c "
import pandas as pd
metrics = pd.read_csv('data/processed/exploratory_metrics.csv')
print('=== MÉTRICAS CLAVE DEL ANÁLISIS ===')
print(f'Total Negocios: {metrics.iloc[0].total_businesses}')
print(f'Total Productos: {metrics.iloc[0].total_products}')
print(f'Total Transacciones: {metrics.iloc[0].total_transactions}')
print(f'Valor Inventario: ${metrics.iloc[0].total_inventory_value:,.0f}')
print(f'Industria más común: {metrics.iloc[0].most_common_industry}')
print(f'Categoría más valiosa: {metrics.iloc[0].most_valuable_inventory_category}')
"
```

#### Opción 3: Ver Visualizaciones Generadas
```bash
# Las visualizaciones están guardadas en:
ls reports/images/
# Incluye: business_distribution.png, product_analysis.png, stock_analysis.png, 
#          temporal_analysis.png, seasonal_heatmap.png, business_analysis.png,
#          warehouse_analysis.png, correlation_matrix.png
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

### ✅ **Fase 3: Análisis Exploratorio** (Completada) 🎉
- [x] Notebook de análisis exploratorio completo
- [x] Estadísticas descriptivas avanzadas
- [x] Identificación de patrones y tendencias
- [x] 8 visualizaciones profesionales generadas
- [x] Métricas clave exportadas y documentadas

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

### 📅 **Fase 7: Documentación Final** (En progreso)
- [x] Documentación técnica completa actualizada
- [ ] Módulos de análisis reutilizables
- [ ] Presentación de resultados finales

---

## 🏆 Resultados Obtenidos

### 📊 **Análisis Exploratorio Completado**

El proyecto ha alcanzado exitosamente los objetivos del **Análisis Exploratorio de Datos**, generando insights valiosos sobre el comportamiento del inventario multi-tenant de GESTOCK.

#### **🎯 Logros Principales**

##### **1. Generación de Datos Realistas**
- ✅ **Datasets completos**: 1,900 transacciones en 6 meses de histórico
- ✅ **Integridad referencial**: 100% de consistencia entre tablas
- ✅ **Patrones realistas**: Estacionalidad, actividad horaria y semanal
- ✅ **Multi-tenant**: 8 negocios en diferentes industrias

##### **2. Análisis Comprehensivo**
- ✅ **Análisis descriptivo**: Estadísticas completas de todos los datasets
- ✅ **Análisis temporal**: Patrones estacionales y tendencias identificadas
- ✅ **Análisis multidimensional**: Comparativas por negocio, almacén y categoría
- ✅ **Análisis de correlaciones**: Relaciones entre variables clave

##### **3. Visualizaciones Profesionales**
- ✅ **8 gráficos de alta calidad** exportados como PNG
- ✅ **Distribución de negocios** por industria, tamaño y ubicación
- ✅ **Análisis de productos** con precios, categorías y márgenes
- ✅ **Análisis de stock** con valores de inventario y distribución
- ✅ **Análisis temporal** con patrones horarios, semanales y estacionales
- ✅ **Heatmaps estacionales** por categoría de producto
- ✅ **Análisis comparativo** entre tipos de negocio y almacenes
- ✅ **Matrices de correlación** entre variables clave

#### **📈 Insights Clave Identificados**

##### **Patrones de Negocio**
- **Construcción**: Industria más común y más estacional
- **Distribuidoras**: Tipo de negocio más activo transaccionalmente
- **Electrónicos**: Categoría de mayor valor en inventario ($69.8 mil millones)
- **Jueves 9:00 AM**: Momento de pico de actividad

##### **Optimizaciones Identificadas**
- **Stock concentrado**: Electrónicos requieren gestión especializada
- **Patrones estacionales claros**: Construcción pico enero-abril
- **Eficiencia por almacén**: Identificados almacenes de alta/baja rotación
- **Oportunidades de benchmarking**: Mejores prácticas entre tipos de negocio

#### **💾 Datos Exportados**
- ✅ **exploratory_metrics.csv**: 19 métricas clave del análisis
- ✅ **business_analysis.csv**: Análisis detallado por negocio
- ✅ **warehouse_analysis.csv**: Análisis de eficiencia por almacén
- ✅ **stock_with_prices.csv**: Dataset enriquecido con valores de inventario

### 🎓 **Valor Académico Alcanzado**

El proyecto demuestra competencias avanzadas en:
- **Ciencia de Datos**: Manipulación, análisis y visualización de datasets complejos
- **Pensamiento Analítico**: Identificación de patrones y generación de insights
- **Programación Python**: Uso profesional de pandas, matplotlib, seaborn
- **Documentación Técnica**: Notebooks estructurados y documentación completa
- **Aplicación Empresarial**: Solución de problemas reales de inventario

---

## 📞 Información del Proyecto

### 👥 Equipo de Desarrollo
- **Desarrollado por**: GESTOCK 
- **Institución**: CESDE - Nuevas Tecnologías
- **Tipo**: Proyecto Integrador

### 📅 Timeline
- **Inicio**: Octubre 2025
- **Análisis Completado**: 30 de Octubre 2025
- **Estado Actual**: ✅ Fase 3 Completada - Análisis Exploratorio Exitoso
- **Próximo**: Documentación final y presentación

### 🔗 Enlaces
- **Repositorio**: [github.com/Lujan2408/gestock_data_analysis](https://github.com/Lujan2408/gestock_data_analysis)
- **GESTOCK Backend**: Sistema base de gestión de inventario
- **Documentación Técnica**: Ver README.md principal

---

## 📄 Licencia

Este proyecto es desarrollado como **Proyecto Académico** para CESDE - Nuevas Tecnologías.

---

<div align="center">

**⭐ Proyecto desarrollado - Octubre 2025 ⭐**

Desarrollado con ❤️ para optimizar la gestión de inventarios mediante análisis de datos

</div>