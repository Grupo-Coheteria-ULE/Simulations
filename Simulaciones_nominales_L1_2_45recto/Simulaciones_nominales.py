# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 15:19:12 2026

@author: julfe
"""

# CODIGO PARA SIMULACIONES NOMINALES (vuelo vertical sin viento a nivel del mar, para calcular esfuerzos maximos)

from rocketpy import Rocket, Environment, SolidMotor, GenericMotor, Flight

print("--------------------------------------------------------------------------------")

latitud_alcolea = 41.73007275912096

longitud_alcolea = 0.10426577877432051

env = Environment(latitude=latitud_alcolea, longitude=longitud_alcolea, elevation = 186)  # elevación cero porque es a nivel del mar, es en el teleno por que si
env.set_elevation("Open-Elevation") # esto te setea la elevacion en la elevacion en esas coordenadas

env.set_atmospheric_model(type="standard_atmosphere") 

env.info()

print("--------------------------------------------------------------------------------")
# =============================================================================
# Cesaroni_614I100-17A
# =============================================================================
Motor = GenericMotor(
    thrust_source=r"C:\Users\julfe\Documents\GCULE\Simulacion\Simulaciones_nominales_L1_2_45recto\Cesaroni_614I100-17A.csv", 
    burn_time=(0,6.2), # segundos, introducir el rango de tiempo de combustión sgún aparece en la primera columna del archivo csv
    chamber_radius= 0.027, # radio del motor
    chamber_height= 0.236, # longitud del motor sin contar tobera
    chamber_position= 0, # longitud hasta el culo del motor (desde el culo del cohete, que suele ser la tobera)
    propellant_initial_mass = 0.350, # Kg
    nozzle_radius= 0, 
    dry_mass= 0.457, # kg, masa del motor despues del burn out (sin combustible)
    center_of_dry_mass_position= 0.236/2, # posición de la mitad del motor aprox desde la salida de la tobera
    dry_inertia=(0.00389,0.00389,0.000294152), # KG.M2 con peso en seco, calcular momento de inercia de un cilindro de estas dimensiones y misma masa en seco, se hace en esta pagina web https://www.calcuvio.com/momento-inercia-cilindro
    nozzle_position=0,# 0 si no hay tobera
    coordinate_system_orientation="nozzle_to_combustion_chamber" 
)

Motor.info()
print("--------------------------------------------------------------------------------")

Leon_1_2 = Rocket(
    radius = 0.04, # m, radio exterior
    mass = 3.184, # kg, sin motor
    inertia = (0.4463, 0.4463, 0.004573), # kg*m2, misma asunción que para el motor
    power_off_drag = r"C:\Users\julfe\Documents\GCULE\Simulacion\Simulaciones_nominales_L1_2_45recto\curva_drag_L1_2_45_recto.csv", # ruta de .csv drag RASAERO, pasar a comas
    power_on_drag = r"C:\Users\julfe\Documents\GCULE\Simulacion\Simulaciones_nominales_L1_2_45recto\curva_drag_L1_2_45_recto.csv", # misma ruta que arriba
    center_of_mass_without_motor = 0.576955, # posición del cg en m desde la cola
    coordinate_system_orientation = "tail_to_nose", # dejar como esta
)

# añadir punta
punta_1 = Leon_1_2.add_nose(
    length= 0.26,# longitud ojiva
    kind="tangent", 
    position= 1.282 # longitud total cohete
)

# añadir aletas
aletas_1 = Leon_1_2.add_trapezoidal_fins(
    n=4,
    root_chord = 0.16,
    tip_chord = 0.08,  
    span = 0.08,
    position = 0.178, # cuerda en la raíz + desplazamiento 
    sweep_angle = 45
)
print("=====SIN EL MOTOR=====")
Leon_1_2.draw()
Leon_1_2.info()
print("--------------------------------------------------------------------------------")

Leon_1_2.add_motor(Motor, position=0) # la posición es la longitud de la tobera negativa, poner 0 si no se conoce

print("=====CON EL MOTOR=====")
Leon_1_2.draw()
Leon_1_2.info()
Leon_1_2.plots.static_margin()
Leon_1_2.plots.stability_margin()
print("--------------------------------------------------------------------------------")

main = Leon_1_2.add_parachute(
    name="main",
    cd_s=0.915,
    trigger="apogee",      # ejection altitude in meters
    lag = 1.5 # tiempo despues de apogeo hasta 17s + 1 segundo de lo que se tarda en abrir (va a haber que bajarlo porque sino 30m/s es demasiado)
)

test_flight = Flight(
    rocket=Leon_1_2, 
    environment=env, 
    rail_length=2.5, 
    inclination=85, 
    heading=0 
    )

print("---------------------------------------------------------------------------")
test_flight.prints.initial_conditions()
print("---------------------------------------------------------------------------")
test_flight.prints.surface_wind_conditions()
print("---------------------------------------------------------------------------")
test_flight.prints.launch_rail_conditions()
print("---------------------------------------------------------------------------")
test_flight.prints.out_of_rail_conditions()
print("---------------------------------------------------------------------------")
test_flight.prints.burn_out_conditions()
print("---------------------------------------------------------------------------")
test_flight.prints.apogee_conditions()
print("---------------------------------------------------------------------------")
test_flight.prints.events_registered()
print("---------------------------------------------------------------------------")
test_flight.prints.impact_conditions()
print("---------------------------------------------------------------------------")
test_flight.prints.maximum_values()
print("---------------------------------------------------------------------------")

test_flight.plots.trajectory_3d()
test_flight.plots.linear_kinematics_data()
test_flight.plots.flight_path_angle_data()
test_flight.plots.attitude_data()
test_flight.plots.angular_kinematics_data()
test_flight.plots.aerodynamic_forces()
test_flight.plots.fluid_mechanics_data()
test_flight.plots.stability_and_control_data()