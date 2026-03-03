from rocketpy import Rocket, SolidMotor

#---
# 1. Definimos el motor
#----

# Necesito el archivo .eng con la curva de empuje.

# SolidMotor define como empuja el cohete.
# Rocket define la forma y peso (inerciaI, inecriaZ, drag-power_off_drag)
# add_trapezoidal_fins: aletas. Tienen que estar bien posicionadas respecto al centro de masa.
motor = SolidMotor( 
    thrust_source= #ARCHIVO DE EMPUJE (.eng), 
    burn_time = # Tiempo total de quemado,
    
    #MASA E INERCIA
    dry_mass = # Masa del motor vacío (kg), 
    dry_inertia = # INERCIA (Ixx, Iyy, Izz) en kg*m², 
    
    # GEOMETRÍA TOBERA
    nozzle_radius = # Radio de la tobera (m), 
    throat_radius = # Radio del cuello de la tobera
    
    # GEOMETRÍA COMBUSTIBLE (granos)
    grain_number = # Número de granos, 
    grain_density = # Densidad del combustible (kg/m³), 
    grain_outer_radius = # Radio exterior del combustible (m), 
    grain_initial_inner_radius = # Radio interior del combustible (m), 
    grain_initial_height = # Altura de cada grano (m), 
    grain_separation = # Separación entre granos (m),
    
    # POSICIONES FÍSICAS RESPECTO AL TOPE DEL MOTOR
    grains_center_of_mass_position = # Centro de Masa de los granos (m), 
    center_of_dry_mass_position = # Centro de Masa del motor vacío (m),
    interpolation_method = "linear" # Para interpolar el .eng
    )

print("Motor Cargado Correctamente")
print(f"Masa inicial del combustible: {motor.inicial_propellant_mass:.2f} kg")
print(f"Empuje Máximo: {max(motor.thrust_curve)} N")
print(f"Impulso total estimado: {motor.total:impulse:.2f} Ns")

#---
# 2. Definimos el cohete (Rocket)
#---

rocket = Rocket(
    radius = # Radio del Cohete (m),
    mass = # Masa SIN Motor(kg),
    inertia = # (lxx=lyy, lxx=lyy, lzz) Inercia respecto al centro de masa sin motor,
    power_off_drag = # RUTA AL DRAG APAGADO .csv (Curva de drag (.csv)), 
    power_on_drag = # RUTA AL DRAG ENCENDIDO .csv (Curva de drag (csv.)), 
    center_of_mass_without_motor = # posición del Centro de Masa sin motor respecto a la tobera (m)
    )

#---
# 3. Estabilidad (Ojiva y Aletas)
#----
rocket.set_rail_buttons(#,#) # Posición botones de la rampa (m)

# Aletas Trapezoidales
rocket.add_trapezoidal_fins(
    n=, # Número de aletas
    root_chord=, # Cuerda raíz (m)
    tip_chord=, # Cuerda punta (m)
    span=, # Envergadura (m)
    distance_from_cm= # Posición respecto al centro de masa (m)
)

# Ojiva
rocket.add_nose(
    length=, # Longitud de la ojiva (m)
    kind="ogive", # el tipo de ojiva
    distance_from_cm= # distancia al centro de masa
)

# get_rocket() para conseguirlos desde otro archivo.
def get_rocket():
    """Devuelve el cohete y el motor definidos."""
    return rocket, motor






























