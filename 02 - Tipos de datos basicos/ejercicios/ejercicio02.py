# una persona quiere saber cual sera su calificacion final
# la nota sale de:
# el 55% del promedio de sus tres calificaciones parciales
# el 30% de la calificacion del examen final
# el 15% de la calificacion de un trabajo final

partial1 = float(input("Dime la nota del parcial 1: "))  # Pide la nota del primer parcial y la convierte a decimal
partial2 = float(input("Dime la nota del parcial 2: "))  # Pide la nota del segundo parcial y la convierte a decimal
partial3 = float(input("Dime la nota del parcial 3: "))  # Pide la nota del tercer parcial y la convierte a decimal
examen = float(input("Dime la nota del examen: "))  # Pide la nota del examen final y la convierte a decimal
trabajo = float(input("Dime la nota del trabajo: "))  # Pide la nota del trabajo final y la convierte a decimal

# Calcula la nota final según los porcentajes dados:
# 55% del promedio de los parciales, 30% del examen y 15% del trabajo
nota = ((partial1 + partial2 + partial3)/3  # Calcula el promedio de los parciales
        * 0.55 + 0.3 * examen + 0.15 * trabajo)  # Aplica los porcentajes y suma los resultados

print ("nota final: %.2f" % nota)  # Imprime la nota final formateada con dos decimales