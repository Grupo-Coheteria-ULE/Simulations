Módulo de Configuración Atmosférica (Environment)

Este módulo gestiona la creación y parametrización de entornos atmosféricos para las simulaciones de vuelo utilizando la librería RocketPy. Su función principal es transformar datos meteorológicos brutos (formato CSV de ERA5) en modelos físicos tridimensionales.
Relevancia en el Análisis de Monte Carlo

El Análisis de Monte Carlo es una técnica estadística que permite predecir la dispersión de los puntos de impacto y el comportamiento del cohete ante la incertidumbre. Este código es el motor de variabilidad de dichas simulaciones por las siguientes razones:

    Modelado de Incertidumbre Climática: En lugar de utilizar una atmósfera estática, el código permite iterar sobre cientos de perfiles reales de viento, temperatura y presión.

    Cálculo de la Elipse de Caída: Al ejecutar el modelo de cohete sobre la lista de entornos generada, se obtiene una distribución de puntos de impacto que define el área de seguridad necesaria en el Campo de Tiro del Teleno.

    Análisis de Estabilidad: Permite verificar si el margen estático del cohete se mantiene dentro de los límites de seguridad bajo diferentes gradientes de viento vertical.

Documentación de Funciones
1. get_dates(archivo_era5, columna)

Extrae los instantes temporales únicos del conjunto de datos.

    Descripción: Lee el archivo de datos meteorológicos y genera una lista de fechas/horas sin duplicados.

    Parámetros:

        archivo_era5 (str): Ruta al archivo de datos en formato CSV.

        columna (int): Índice de la columna que contiene la estampa temporal (valid_time).

    Lógica: Utiliza el método unique() para asegurar que, aunque existan múltiples registros de presión para una misma hora, solo se genere un punto de entrada por cada perfil vertical completo.

2. create_environment(archivo_era5, latitud, longitud, elevacion, fecha=None)

Construye un objeto de entorno individual.

    Descripción: Instancia la clase Environment de RocketPy y configura el modelo atmosférico personalizado.

    Parámetros:

        latitud / longitud (float): Coordenadas geográficas del punto de lanzamiento.

        elevacion (float): Altitud sobre el nivel del mar en metros.

        fecha (datetime/str): Instante específico para el cual se desea extraer el perfil meteorológico del archivo.

    Configuración del Modelo: Mapea las variables del CSV de la siguiente forma:

        altitude: Asociado a pressure_level (hPa).

        wind_velocity_x / y: Componentes vectoriales u, v (m/s).

        temperature: Temperatura absoluta (K).

3. get_multiple_env(archivo_era5, latitud, longitud, elevacion, columna)

Generador de escenarios en lote.

    Descripción: Automatiza la creación de una lista de objetos Environment recorriendo todas las fechas extraídas del dataset.

    Retorno: Una lista de objetos listos para ser procesados por el motor de simulación de vuelo.

Especificaciones del Dataset (ERA5)

Para asegurar la compatibilidad con este módulo, los archivos de datos deben contener perfiles verticales organizados por niveles de presión. El diccionario de mapeo interno espera las siguientes etiquetas:
Variable	Descripción	Unidad
valid_time	Marca de tiempo del registro	ISO 8601
pressure_level	Nivel de presión atmosférica	hPa
u	Velocidad del viento zonal (Este-Oeste)	m/s
v	Velocidad del viento meridional (Norte-Sur)	m/s
t	Temperatura ambiente	K
r	Humedad relativa	%
Ejemplo de Implementación
Python

from environment import get_multiple_env

# Generar lista de entornos para simulación de dispersión
escenarios = get_multiple_env(
    archivo_era5="data/era5_teleno_julio.csv",
    latitud=42.38,
    longitud=-6.20,
    elevacion=1100,
    columna=0
)

# Acceso a un escenario específico para inspección
escenarios[0].all_info_plots()
