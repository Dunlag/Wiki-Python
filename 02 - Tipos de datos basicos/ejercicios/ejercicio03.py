# dados dos valores A y B intercambiar sus valores y muestralos al final

a = int(input("Dime el numero a: "))  # Pide al usuario el valor de 'a' y lo convierte a entero
b = int(input("Dime el numero b: "))  # Pide al usuario el valor de 'b' y lo convierte a entero

c = a  # Guarda el valor original de 'a' en una variable temporal 'c'

a = b  # Asigna el valor de 'b' a 'a', sobrescribiendo el valor original de 'a'
b = c  # Asigna el valor original de 'a' (guardado en 'c') a 'b', completando el intercambio

print("el valor de a es: ", a)  # Imprime el nuevo valor de 'a'
print("el valor de b es:", b)  # Imprime el nuevo valor de 'b'