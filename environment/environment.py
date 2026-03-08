from rocketpy import Environment
import pandas as pd


def get_dates(archivo_era5, columna):
    data = pd.read_csv(archivo_era5)
    dates_list = data[columna].tolist()
    return dates_list


def get_multiple_env(archivo_era5, latitud, longitud, elevacion, columna, fecha=None):
    dates_list = get_dates(archivo_era5, columna)
    list_environments = []
    for date in dates_list:
        env = create_environment(
            archivo_era5=archivo_era5,
            latitud=latitud,
            longitud=longitud,
            elevacion=elevacion,
            fecha=date
        )
        list_environments.append(env)
    return list_environments
        


# Si no proporcionamos una fecha al environment se utilizará la fecha y hora de la primera entrada cronológica del dataset.
def create_environment(archivo_era5, latitud, longitud, elevacion, fecha=None):

    # Utilizar coordenadas del lugar de lanzamiento
    env = Environment(latitude=latitud, longitude=longitud, elevation=elevacion) # Creamos el objeto Environment

    if fecha is not None:
        env.set_date(fecha)

    # Cargamos los datos meteorológicos que hemos extraido de ERA5
    env.set_atmospheric_model(
        type='custom_atmosphere', # para proporcionar nuestros propios datos
        file=str(archivo_era5),
        dictionary={
            "altitude": "z",           # Altitud en metros
            "temperature": "t",        # Temperatura en K
            "wind_velocity_x": "u",    # Componente zonal (Este - Oeste) (m/s)
            "wind_velocity_y": "v",    # Componente meridional (Norte - Sur) (m/s)
            "relative_humidity": "r"   # Humedad relativa
        }
    )

    return env


def main():

    ruta = input("Introduce la ruta de tu dataset:\n")
    columna = int(input("¿Podría especificar la columna donde se encuentran las fechas/horas en el dataset?"))
    latitud = float(input("Introduce la altitud:\n"))
    longitud = float(input("Introduce la longitud\n"))
    elevacion = float(input("Introduce la elevacion:\n"))

    list_environments = get_multiple_env(ruta, latitud, longitud, elevacion, columna)

    print("Lista con todos los environments cargada corréctamente!")


if __name__ == "__main__":
    main()