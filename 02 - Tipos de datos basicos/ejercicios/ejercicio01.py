# Dados los catetos de un triangulo rectangulo
# calcula su hipotenusa

import math  # Importa el módulo 'math' para usar la función de raíz cuadrada (sqrt)

cateto1 = float(input("Introduce el cateto 1:"))  # Pide al usuario que ingrese el valor del primer cateto y lo convierte a un número decimal (float)
cateto2 = float(input("Introduce el cateto 2:"))  # Pide al usuario que ingrese el valor del segundo cateto y lo convierte a un número decimal (float)

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)  # Calcula la hipotenusa usando el teorema de Pitágoras: hipotenusa = raíz cuadrada (cateto1^2 + cateto2^2)

print("la hipotenusa es %.2f" % hipotenusa)  # Imprime el resultado de la hipotenusa, formateado a dos decimales