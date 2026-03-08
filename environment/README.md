# Modulo de Configuracion Atmosferica (Environment)

Este modulo gestiona la creacion y parametrizacion de entornos atmosfericos para las simulaciones de vuelo utilizando la libreria RocketPy. Su funcion principal es transformar datos meteorologicos brutos (formato CSV de ERA5) en modelos fisicos tridimensionales.

## Relevancia en el Analisis de Monte Carlo

El Analisis de Monte Carlo es una tecnica estadistica que permite predecir la dispersion de los puntos de impacto y el comportamiento del cohete ante la incertidumbre. Este codigo es el motor de variabilidad de dichas simulaciones por las siguientes razones:

1. Modelado de Incertidumbre Climatica: En lugar de utilizar una atmosfera estatica, el codigo permite iterar sobre cientos de perfiles reales de viento, temperatura y presion.
2. Calculo de la Elipse de Caida: Al ejecutar el modelo de cohete sobre la lista de entornos generada, se obtiene una distribucion de puntos de impacto que define el area de seguridad necesaria en el Campo de Tiro del Teleno.
3. Analisis de Estabilidad: Permite verificar si el margen estatico del cohete se mantiene dentro de los limites de seguridad bajo diferentes gradientes de viento vertical.

---

## Documentacion de Funciones

### 1. get_dates(archivo_era5, columna)
Extrae los instantes temporales unicos del conjunto de datos.
* Descripcion: Lee el archivo de datos meteorologicos y genera una lista de fechas/horas sin duplicados.
* Parametros:
    * archivo_era5 (str): Ruta al archivo de datos en formato CSV.
    * columna (int): Indice de la columna que contiene la estampa temporal (valid_time).
* Logica: Utiliza el metodo unique() para asegurar que, aunque existan multiples registros de presion para una misma hora, solo se genere un punto de entrada por cada perfil vertical completo.

### 2. create_environment(archivo_era5, latitud, longitud, elevacion, fecha=None)
Construye un objeto de entorno individual.
* Descripcion: Instancia la clase Environment de RocketPy y configura el modelo atmosferico personalizado.
* Parametros:
    * latitud / longitud (float): Coordenadas geograficas del punto de lanzamiento.
    * elevacion (float): Altitud sobre el nivel del mar en metros.
    * fecha (datetime/str): Instante especifico para el cual se desea extraer el perfil meteorologico del archivo.
* Configuracion del Modelo: Mapea las variables del CSV de la siguiente forma:
    * altitude: Asociado a pressure_level (hPa).
    * wind_velocity_x / y: Componentes vectoriales u, v (m/s).
    * temperature: Temperatura absoluta (K).

### 3. get_multiple_env(archivo_era5, latitud, longitud, elevacion, columna)
Generador de escenarios en lote.
* Descripcion: Automatiza la creacion de una lista de objetos Environment recorriendo todas las fechas extraidas del dataset.
* Retorno: Una lista de objetos listos para ser procesados por el motor de simulacion de vuelo.

---

## Especificaciones del Dataset (ERA5)

Para asegurar la compatibilidad con este modulo, los archivos de datos deben contener perfiles verticales organizados por niveles de presion. El diccionario de mapeo interno espera las siguientes etiquetas:

- valid_time: Marca de tiempo del registro (ISO 8601).
- pressure_level: Nivel de presion atmosferica (hPa).
- u: Velocidad del viento zonal Este-Oeste (m/s).
- v: Velocidad del viento meridional Norte-Sur (m/s).
- t: Temperatura ambiente (K).
- r: Humedad relativa (%).

---

## Ejemplo de Implementacion

from environment import get_multiple_env

# Generar lista de entornos para simulacion de dispersion
escenarios = get_multiple_env(
    archivo_era5="data/era5_teleno_julio.csv",
    latitud=42.38,
    longitud=-6.20,
    elevacion=1100,
    columna=0
)

# Acceso a un escenario especifico para inspeccion
escenarios[0].all_info_plots()