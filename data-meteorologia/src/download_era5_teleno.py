import cdsapi # cliente oficial Copernicus Climate Data storage para descargar ERA 5
from datetime import datetime, timedelta # para manejar fechas y dividir Julio en semanas 

c = cdsapi.Client() # con estos creamos una conexión con ~/.cdsapirc donde almacenamos nuestra clave API CDS (nuestra cuenta)

def get_week(start_date, month, year): # con esta función generamos listas de máximo 7 días desde fecha de inicio del mes. 
    """Genera lista de 7 días max desde start_date"""
    days = []
    current = datetime(int(year), int(month), int(start_date)) # fecha inicio
    end_week = current + timedelta(days=6) # fecha fin de semana
    for d in range(current.day, end_week.day + 1): # iteramos entre días
        if current.month == int(month): # verificamos no salirnos de julio
            days.append(f'{current.day:02d}')
            current += timedelta(days=1) # avanza al día siguiente
        else:
            break
    return days

# Parámetros
years = ['2024', '2025'] # años de los que extraemos los datos
month = '07' # julio
start_days = ['01', '08', '15', '22', '29']  # Inicio semanas julio
times = [f'{h:02d}:00' for h in range(24)]

for year in years: # 2024, 2025
    for week_start in start_days: # generamos 10 request para no sobrepasar el límite de ERA5
        days = get_week(week_start, month, year)
        if days:
            filename = f'era5_teleno_{year}_{month}_week_{week_start}.nc'
            print(f"Descargando {year}-{month}, semana desde {week_start}: {days}")
            
            c.retrieve( # REQUEST
                'reanalysis-era5-pressure-levels',
                {
                    'product_type': 'reanalysis',
                    'variable': [
                        'u_component_of_wind',
                        'v_component_of_wind',
                        'temperature',
                        'relative_humidity',
                    ],
                    'pressure_level': ['1000', '925', '850', '700', '500'],
                    'year': year,
                    'month': month,
                    'day': days,
                    'time': times,
                    'area': [42.35, -6.45, 42.25, -6.35],
                    'format': 'netcdf',
                },
                filename,
            )
            print(f"¡Listo: {filename}")
