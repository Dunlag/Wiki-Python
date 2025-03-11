# pedir el nombre y los dos apellidos
# de una persona y mostrar sus iniciales

nombre = input("dime tu nombre ")  # Pide al usuario que ingrese su nombre
apellido1 = input("dime tu primer apellido ")  # Pide al usuario que ingrese su primer apellido
apellido2 = input("dime tu segundo apellido ")  # Pide al usuario que ingrese su segundo apellido

inicial = nombre[0]  # Obtiene la primera letra del nombre
inicial = inicial + apellido1[0]  # Añade la primera letra del primer apellido
inicial = inicial + apellido2[0]  # Añade la primera letra del segundo apellido

print(inicial.upper())  # Imprime la cadena que contiene las iniciales