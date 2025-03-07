# Datos y Tipos de Datos en Python 3

En Python, todo dato tiene un tipo asociado. Conocer los tipos de datos es fundamental para manipular correctamente la información en un programa.

---

## Tipos de Datos Básicos en Python

Python tiene varios tipos de datos predefinidos:

### 1. Números (`int`, `float`, `complex`)
- **Enteros (`int`)**: Números sin decimales.
- **Flotantes (`float`)**: Números con decimales.
- **Complejos (`complex`)**: Números con parte real e imaginaria.

Ejemplo:

```python
entero = 42
flotante = 3.14
complejo = 2 + 3j

print(type(entero))   # <class 'int'>
print(type(flotante)) # <class 'float'>
print(type(complejo)) # <class 'complex'>
```

---

## Datos Numéricos en Python

Los números en Python pueden ser enteros (`int`), flotantes (`float`) o complejos (`complex`).

### Operaciones Matemáticas Básicas

```python
num = -5
print(abs(num))  # Valor absoluto -> 5

print(7 / 2)   # División normal -> 3.5
print(7 // 2)  # División entera -> 3
print(7 % 2)   # Módulo (resto) -> 1

print(3**2)    # Potencia -> 9
print(pow(3,2)) # Otra forma de elevar al cuadrado -> 9
```

### Conversión de Tipos Numéricos

```python
a = int(7.2)
print(a)  # 7

b = float(a)
print(b)  # 7.0
```

**¡Cuidado con convertir cadenas a números!**

```python
a = int("234")  # Esto funciona

# a = int("abs")  # Esto generará un error
# ValueError: invalid literal for int() with base 10: 'abs'
```

### Funciones Matemáticas

```python
print(divmod(7,2))  # (3, 1) -> Devuelve cociente y resto

import math
print(math.sqrt(9))  # Raíz cuadrada -> 3.0
```

---

## Tips y Consejos
- Usa `abs(n)` para obtener el valor absoluto.
- `//` es útil si solo necesitas la parte entera de una división.
- `divmod(a, b)` devuelve el cociente y el resto en una sola llamada.
- La conversión de `int` a `float` es segura, pero convertir cadenas requiere precaución.

---
