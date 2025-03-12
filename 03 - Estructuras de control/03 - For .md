# Bucle `for` en Python

El bucle `for` en Python se utiliza para iterar sobre una secuencia (como una lista, una tupla, un diccionario, un conjunto o una cadena de caracteres) o para ejecutar un bloque de código un número determinado de veces.

## Sintaxis básica

```python
for variable in iterable:
    # Bloque de código a ejecutar en cada iteración
```

### Ejemplo: Recorrer una lista
```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```
**Salida:**
```
manzana
banana
cereza
```

### Uso de `range()` en un `for`
La función `range()` permite generar una secuencia de números para iterar sobre ellos.

```python
for num in range(1, 11, 2):
    print(num, " ", end="")
```
**Salida:**
```
1 3 5 7 9 
```

- `range(1, 11, 2)`: genera los números del 1 al 10, con un paso de 2.

### Iterar sobre una cadena de caracteres
```python
for letra in "Python":
    print(letra, end=" ")
```
**Salida:**
```
P y t h o n 
```

### `for` con diccionarios
Podemos recorrer las claves y valores de un diccionario:
```python
edades = {"Ana": 25, "Luis": 30, "Pedro": 20}
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")
```
**Salida:**
```
Ana tiene 25 años
Luis tiene 30 años
Pedro tiene 20 años
```

## Uso de `break` y `continue` en `for`

- `break`: finaliza el bucle antes de que termine todas las iteraciones.
- `continue`: salta a la siguiente iteración sin ejecutar el resto del código dentro del bucle.

### Ejemplo con `break`
```python
for num in range(1, 10):
    if num == 5:
        print("Se encontró el 5, deteniendo el bucle.")
        break
    print(num)
```
**Salida:**
```
1
2
3
4
Se encontró el 5, deteniendo el bucle.
```

### Ejemplo con `continue`
```python
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
```
**Salida:**
```
1
2
4
5
```

## Consejos y buenas prácticas 🛠️
✅ Usa `enumerate()` si necesitas el índice y el valor en un `for`.
✅ Evita modificar la secuencia sobre la que estás iterando.
✅ Prefiere `for` sobre `while` cuando sepas cuántas veces iterar.
✅ Usa list comprehensions para crear listas de forma más eficiente:
```python
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]
```

El bucle `for` es una herramienta poderosa en Python, permitiendo escribir código más limpio y eficiente. ¡Pruébalo y sigue practicando! 🚀

