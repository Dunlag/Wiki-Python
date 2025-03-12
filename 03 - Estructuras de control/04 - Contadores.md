# Contadores, Acumuladores e Indicadores en Python

En la programación, es común necesitar llevar un registro de valores, ya sea contando eventos, sumando valores o marcando ciertas condiciones. Para ello, utilizamos **contadores, acumuladores e indicadores**.

---

## Contadores
Un contador es una variable que se incrementa o decrementa en un valor fijo dentro de un bucle. Se usa para contar eventos, como la cantidad de veces que ocurre algo.

### Ejemplo de contador
```python
cont = 0  # Inicializamos el contador
for var in range(1, 4):
    num = int(input("Dime un número: "))
    if num % 2 == 0:
        cont = cont + 1  # Incrementamos el contador si el número es par

if cont == 1:
    print("Has introducido un único número par")
else:
    print("Has introducido", cont, "números pares")
```
### Explicación:
1. `cont = 0`: Se inicializa el contador en 0.
2. Se solicita tres números al usuario dentro del bucle `for`.
3. Si el número es par, `cont` se incrementa en 1.
4. Al final, se muestra cuántos números pares se introdujeron.

### Tip:
Si queremos restar en lugar de sumar, podemos hacer `cont = cont - 1` o usar `cont -= 1`.

---

## Acumuladores
Un **acumulador** es similar a un contador, pero en lugar de aumentar en un valor fijo, se le suman valores variables.

### Ejemplo de acumulador
```python
total = 0  # Inicializamos el acumulador
for i in range(5):
    num = int(input("Introduce un número: "))
    total += num  # Sumamos cada número al total

print("La suma total es:", total)
```

### Explicación:
1. `total = 0`: Se inicializa el acumulador.
2. Se pide al usuario cinco números.
3. Cada número se suma al `total`.
4. Al final, se muestra la suma de todos los números.

### Tip:
Se pueden usar acumuladores para calcular promedios dividiendo por la cantidad de elementos:
```python
promedio = total / 5
print("El promedio es:", promedio)
```

---

## Indicadores
Los **indicadores** son variables que almacenan un estado para verificar si ocurrió algo dentro del bucle.

### Ejemplo de indicador
```python
hay_par = False  # Indicador
for i in range(3):
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        hay_par = True  # Cambiamos el indicador si encontramos un número par

if hay_par:
    print("Se ingresó al menos un número par")
else:
    print("No se ingresaron números pares")
```

### Explicación:
1. `hay_par = False`: Inicializamos el indicador en `False`.
2. Pedimos tres números al usuario.
3. Si encontramos un número par, cambiamos `hay_par` a `True`.
4. Al finalizar el bucle, verificamos si `hay_par` cambió para dar un mensaje adecuado.

### Tip:
Podemos usar más de un indicador para verificar múltiples condiciones a la vez.

---

## Conclusión
Los contadores, acumuladores e indicadores son herramientas clave para gestionar datos en bucles. Usarlos correctamente nos ayuda a optimizar el código y hacer que nuestros programas sean más eficientes. 🚀

