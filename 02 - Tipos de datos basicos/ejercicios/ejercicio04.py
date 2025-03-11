# Pedir la hora, minutos y segundos a la que un ciclista sale de una ciudad y
# también el tiempo que se tarda en llegar en segundos a otra ciudad y calcular
# y mostrar la hora a la que se llegará a esa ciudad

hora_salida = int(input("Hora de salida (0-23): "))  # Pide la hora de salida
minutos_salida = int(input("Minutos de salida (0-59): "))  # Pide los minutos de salida
segundos_salida = int(input("Segundos de salida (0-59): "))  # Pide los segundos de salida
tiempo_viaje_segundos = int(input("Tiempo de viaje en segundos: "))  # Pide el tiempo de viaje en segundos

# Convertir la hora de salida a segundos
total_segundos_salida = hora_salida * 3600 + minutos_salida * 60 + segundos_salida

# Calcular la hora de llegada en segundos
total_segundos_llegada = total_segundos_salida + tiempo_viaje_segundos

# Convertir la hora de llegada de segundos a hora, minutos y segundos
hora_llegada = total_segundos_llegada // 3600  # Calcula la hora de llegada
minutos_llegada = (total_segundos_llegada % 3600) // 60  # Calcula los minutos de llegada
segundos_llegada = total_segundos_llegada % 60  # Calcula los segundos de llegada

# Ajustar la hora de llegada si supera las 24 horas
hora_llegada = hora_llegada % 24

# Mostrar la hora de llegada formateada
print("Hora de llegada: {:02d}:{:02d}:{:02d}".format(hora_llegada, minutos_llegada, segundos_llegada))