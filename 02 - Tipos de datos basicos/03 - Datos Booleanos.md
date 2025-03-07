# Tipos de Datos Booleanos en Python

En Python, los valores booleanos representan dos estados lógicos: `True` (verdadero) y `False` (falso). Son utilizados en estructuras de control como condicionales y bucles para tomar decisiones en un programa.

## 1. Declaración y Uso de Booleanos
Los valores booleanos en Python se representan con las palabras clave `True` y `False`.

```python
valor_verdadero = True
valor_falso = False
print(valor_verdadero)  # Output: True
print(valor_falso)      # Output: False
```

**Tip:** En Python, `True` y `False` deben escribirse con la primera letra en mayúscula. `true` y `false` darán un error.

## 2. Booleanos en Expresiones Lógicas
Los valores booleanos se utilizan para evaluar expresiones lógicas y realizar comparaciones.

```python
print(5 > 3)   # Output: True
print(10 == 20) # Output: False
print(7 <= 7)  # Output: True
```

## 3. Operadores Booleanos
Python proporciona operadores lógicos para combinar valores booleanos:

- `and`: Devuelve `True` si ambas condiciones son verdaderas.
- `or`: Devuelve `True` si al menos una condición es verdadera.
- `not`: Invierte el valor booleano.

```python
print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False
```

**Tip:** `not` es útil para invertir condiciones en estructuras de control.

## 4. Conversión a Booleanos
Cualquier valor en Python puede evaluarse como `True` o `False`. La función `bool()` permite convertir valores a booleanos.

```python
print(bool(0))      # Output: False
print(bool(1))      # Output: True
print(bool(""))    # Output: False
print(bool("Hola")) # Output: True
print(bool([]))     # Output: False (listas vacías son falsas)
print(bool([1,2]))  # Output: True
```

## 5. Uso de Booleanos en Condicionales
Los valores booleanos son esenciales en estructuras de control como `if` y `while`.

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## 6. Ejemplo Práctico
Vamos a escribir un programa que verifique si un usuario tiene acceso según su edad.

```python
edad = int(input("Introduce tu edad: "))
acceso = edad >= 18  # Devuelve True si la edad es 18 o mayor, False en caso contrario

if acceso:
    print("Tienes acceso al sistema.")
else:
    print("Acceso denegado.")
```

**Consejo:** Puedes usar variables booleanas para hacer el código más legible y fácil de entender.

---
### Resumen
- `True` y `False` son los valores booleanos en Python.
- Se usan en expresiones lógicas con operadores como `and`, `or`, y `not`.
- Se pueden obtener booleanos desde otros tipos de datos con `bool()`.
- Son fundamentales en estructuras de control como `if` y `while`.

Ahora que entiendes los booleanos, estarás listo para usarlos en programas más complejos. ¡Sigue adelante! 🚀

