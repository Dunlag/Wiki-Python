# Funciones en Python

Las funciones en Python permiten estructurar el código de manera modular y reutilizable. Se pueden definir con parámetros, devolver valores y hasta ser recursivas. También es importante entender el ámbito de las variables y cómo se pasan los parámetros a las funciones.

## Definiendo una función

En Python, una función se define con la palabra clave `def`, seguida del nombre de la función y paréntesis que pueden incluir parámetros.

```python
# Definición de una función simple
def saludar():
    print("Hola, bienvenido a Python!")

# Llamada a la función
saludar()
```

## Parámetros: formales y reales

Los parámetros formales son los que aparecen en la definición de la función, mientras que los parámetros reales son los que se pasan cuando se llama a la función.

```python
def saludar_persona(nombre):  # Parámetro formal
    print(f"Hola, {nombre}!")

saludar_persona("Fernando")  # Parámetro real
```

## Paso de parámetros por referencia en Python

En Python, los parámetros se pasan siempre por referencia. Sin embargo, los objetos inmutables (como números y cadenas) no pueden modificarse dentro de una función.

```python
def modificar_valor(x):
    x = 10  # Esto no afecta la variable original si x es un número
    print("Dentro de la función:", x)

num = 5
modificar_valor(num)
print("Fuera de la función:", num)  # Sigue siendo 5
```

Pero si el argumento es un objeto mutable, se puede modificar dentro de la función:

```python
def modificar_lista(lista):
    lista.append(4)
    print("Dentro de la función:", lista)

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la función:", mi_lista)  # La lista fue modificada
```

## Variables globales y locales

- **Variables locales:** Se definen dentro de una función y solo pueden usarse dentro de ella.
- **Variables globales:** Se definen fuera de cualquier función y pueden ser accedidas desde cualquier parte del programa.

```python
x = 10  # Variable global

def mostrar():
    x = 5  # Variable local
    print("Dentro de la función:", x)

mostrar()
print("Fuera de la función:", x)  # Sigue siendo 10
```

Si queremos modificar una variable global dentro de una función, usamos `global`:

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1
```

## Funciones recursivas

Una función recursiva es aquella que se llama a sí misma para resolver un problema.

Ejemplo: Cálculo del factorial de un número:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

**Consejo:** Toda función recursiva debe tener un caso base para evitar bucles infinitos.

## Conclusión

Las funciones permiten estructurar el código de forma más clara y reutilizable. Entender el ámbito de las variables y cómo se pasan los parámetros es clave para evitar errores. ¡Practica creando funciones y experimentando con parámetros mutables e inmutables! 🚀

