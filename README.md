**era5_teleno_julio_2425**

 Hemos recopilado datos meteorológicos de ERA5 para el área del Teleno en julio 2024-2025, enfocados en niveles de presión para el vuelo del cohete.
Estos datos permiten modelar vientos y estabilidad útiles para el análisis de misión y zona de caida del cohete en simulaciones con rocketpy.

    Las variables incluidas son las siguientes:

        -> u (componente zonal) : mide el flujo horizontal este-oeste a un nivel de presión dado. 
            Valores positivos indican viento hacia el este (de oeste a este), negativos hacia el oeste. 
            Se mide en m/s a niveles de presión distintos. En este caso, 'u' varía de -10 a +10 m/s.

        -> v (componente meridional): mide el flujo horizontal norte-sur a un nivel de presión dado.
            Valores positivos indican viento hacia el norte (de sur a norte), negativos hacia el sur.
            Se mide en m/s a niveles de presión distintos. En este caso, 'v' varía de -3 a +8 m/s.
        
        -> t (temperatura): mide la temperatura del aire en Kelvin(K) a un nivel de presión dado.
            En este caso 't' varía de 275 a 308 K (2ºC a 35º)
            La temperatura afecta la densidad atmosférica reduciendo empuje y velocidad a una determinada temperatura.
        
        -> r (humedad relativa): representa la humedad relativa en porcentaje respecto al agua (>0ºC) o hielo (<-23ºC), a distintos niveles de presión.
            Valores de 0% indican aire seco. En nuestro dataset, oscila entre 0-10% en la superficie hasta 60-80% en la estratosfera.
            Una 'r' alta baja el empuje del motor. Alta humedad también genera nubes/lluvia en el Teleno, incrementando arrastre de drag y desviando la trayectoria.
            En rocketpy 'relative_humidity(altitude) corrige la presión estática atmosférica.
            Aunque su impacto directo sobre el cohete es el más pequeño comparado con viento, presión y temperatura, también es relevante.

        -> p (presión): la presión decrece exponencialmente con la altura. La presión determina la densidad del aire, clave para calcular el arrastre que frena el cohete:
            más presión = más denso = más arrastre inicial.
            
