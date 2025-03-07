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

### 2. Booleanos (`bool`)
Representan **verdadero** o **falso** (`True` o `False`).

```python
es_mayor = True
es_menor = False
print(type(es_mayor))  # <class 'bool'>
```

### 3. Cadenas de Caracteres (`str`)
Secuencias de caracteres delimitadas por comillas simples o dobles.

```python
mensaje = "Hola, Python!"
print(type(mensaje))  # <class 'str'>
```

Puedes acceder a caracteres específicos con índices:

```python
print(mensaje[0])  # 'H'
print(mensaje[-1]) # '!'
```

### 4. Listas (`list`)
Son estructuras ordenadas y mutables (pueden cambiarse) que almacenan múltiples valores.

```python
numeros = [1, 2, 3, 4, 5]
numeros.append(6)  # Agrega un elemento
print(numeros)     # [1, 2, 3, 4, 5, 6]
```

### 5. Tuplas (`tuple`)
Similares a las listas, pero **inmutables** (no pueden modificarse).

```python
coordenadas = (10, 20)
print(type(coordenadas))  # <class 'tuple'>
```

### 6. Diccionarios (`dict`)
Colecciones de pares clave-valor.

```python
persona = {"nombre": "Juan", "edad": 30}
print(persona["nombre"])  # 'Juan'
```

### 7. Conjuntos (`set`)
Colecciones de elementos **únicos** y **desordenados**.

```python
colores = {"rojo", "verde", "azul"}
colores.add("amarillo")
print(colores)
```

---

## Conversión de Tipos
Puedes convertir entre tipos de datos usando funciones como `int()`, `float()`, `str()`, etc.

```python
num = "42"
num_entero = int(num)  # Convierte a entero
print(num_entero + 10)  # 52
```

---

## Tips y Consejos
- Usa `type(variable)` para verificar el tipo de dato.
- Prefiere **tuplas** si los datos no van a cambiar.
- Utiliza **sets** para eliminar duplicados automáticamente.
- **Diccionarios** son ideales para organizar datos con claves únicas.
