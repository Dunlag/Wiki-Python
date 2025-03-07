
# Guía de Variables y Entrada/Salida Estándar en Python

## 1. Variables en Python

En Python, las variables se utilizan para almacenar valores y hacer referencia a ellos en el programa. No es necesario declarar el tipo de la variable explícitamente, ya que Python es un lenguaje de tipado dinámico.

### 1.1 Asignación de variables

Puedes asignar valores a las variables de la siguiente manera:

```python
x = 5        # Asignación de un número entero
name = "Juan" # Asignación de una cadena de texto (string)
price = 3.99   # Asignación de un número decimal (float)
is_active = True # Asignación de un valor booleano
```

### 1.2 Tipos de datos comunes

- **int**: Números enteros.
- **float**: Números decimales.
- **str**: Cadenas de texto.
- **bool**: Valores booleanos (`True` o `False`).

### 1.3 Operaciones con variables

Puedes realizar operaciones aritméticas con las variables:

```python
x = 10
y = 2

suma = x + y        # 12
resta = x - y       # 8
multiplicacion = x * y  # 20
division = x / y    # 5.0
```

## 2. Entrada estándar (input)

En Python, puedes recibir datos del usuario mediante la función `input()`. Esta función lee la entrada del usuario como una cadena (string), por lo que es importante convertirla al tipo de dato adecuado si es necesario.

### 2.1 Leer entrada del usuario

```python
name = input("¿Cuál es tu nombre? ")
print(f"Hola, {name}!")
```

### 2.2 Convertir entrada a otro tipo

Si el valor introducido necesita ser de otro tipo (por ejemplo, un número entero o decimal), puedes convertirlo usando las funciones `int()` o `float()`.

```python
age = int(input("¿Cuántos años tienes? "))
height = float(input("¿Cuánto mides? (en metros) "))
print(f"Tienes {age} años y mides {height} metros.")
```

## 3. Salida estándar (print)

La función `print()` se usa para mostrar resultados en la consola o salida estándar. Puedes imprimir variables y texto con ella.

### 3.1 Imprimir texto y variables

```python
name = "Carlos"
age = 25
print("Hola, mi nombre es", name, "y tengo", age, "años.")  # Forma básica
```

### 3.2 Usar f-strings (Formateo de cadenas)

Desde Python 3.6, se puede usar la interpolación de cadenas con f-strings para una forma más legible de mostrar variables dentro de una cadena:

```python
name = "Carlos"
age = 25
print(f"Hola, mi nombre es {name} y tengo {age} años.")  # Forma moderna
```

### 3.3 Imprimir múltiples valores

Puedes imprimir múltiples valores en una sola llamada a `print()`, separándolos por comas. Python añadirá automáticamente un espacio entre ellos.

```python
x = 10
y = 20
print("La suma de", x, "y", y, "es", x + y)
```

### 3.4 Personalizar el separador y final de impresión

La función `print()` también permite personalizar el separador entre los elementos y el carácter final de la impresión.

```python
print("Hola", "Mundo", sep="-")  # Usará "-" como separador
print("Este es el primer mensaje.", end=" ")  # No termina con salto de línea
print("Este es el segundo mensaje.")
```

## 4. Resumen

- **Variables**: Puedes almacenar cualquier tipo de datos sin declarar su tipo. Usa operadores aritméticos para trabajar con ellos.
- **Entrada estándar**: Usa `input()` para leer datos del usuario. Recuerda convertir los datos al tipo adecuado.
- **Salida estándar**: Usa `print()` para mostrar resultados. Puedes formatear las salidas con f-strings o personalizar separadores y finales.

---
