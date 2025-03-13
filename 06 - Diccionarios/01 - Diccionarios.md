# Diccionarios en Python

Los diccionarios en Python son estructuras de datos que almacenan pares clave-valor. Son muy útiles cuando se necesita acceder a valores de manera rápida a través de una clave.

## Creación de un diccionario

```python
diccionario = {'one': 1, 'two': 2, 'three': 3}
print(diccionario)
print(type(diccionario))
print(diccionario['two'])
```

## Características de los diccionarios
- Son mutables, lo que significa que se pueden modificar después de su creación.
- No permiten claves duplicadas.
- Son desordenados en versiones anteriores a Python 3.7, pero desde esa versión en adelante mantienen el orden de inserción.

## Agregar y modificar elementos

```python
dict1 = {}
dict1["nombre"] = "jose"
dict1["edad"] = 20
print(dict1)
print(len(dict1))
```

### Eliminar elementos

```python
del diccionario["one"]
print(diccionario)
```

## Métodos principales de los diccionarios

- `clear()`: Borra todos los elementos del diccionario.
- `update()`: Combina dos diccionarios.
- `get()`: Devuelve el valor de una clave si existe, de lo contrario devuelve un valor predeterminado.
- `pop()`: Elimina una clave específica y devuelve su valor.
- `keys()`, `values()`, `items()`: Iteran sobre claves, valores y pares clave-valor respectivamente.

### Ejemplo de uso:

```python
dict1.clear()
print(dict1)

dict1 = {'one': 1, 'two': 2, 'three': 3}
dict2 = {'four': 4, 'five': 5, 'six': 6}

dict1.update(dict2)
print(dict1)
```

### Acceder a valores de forma segura

```python
print(dict1.get("one"))  # Devuelve 1
print(dict1.get("ones", "no existe"))  # Devuelve "no existe"
```

### Eliminar elementos con `pop()`

```python
dict1.pop("one")
dict1.pop("seven", "no existe")  # Devuelve "no existe"
```

## Iterar sobre un diccionario

```python
for clave in dict1.keys():
    print(clave)

for valor in dict1.values():
    print(valor)

for clave, valor in dict1.items():
    print(clave, valor)
```

## Consejos y Tips ✨
✅ Usa `get()` en lugar de `[]` para evitar errores si la clave no existe.
✅ Recuerda que las claves deben ser inmutables (strings, números o tuplas).
✅ `update()` es útil para fusionar diccionarios de manera eficiente.
✅ Usa `dict1.copy()` si quieres hacer una copia sin modificar el original.

Los diccionarios son una herramienta poderosa en Python para organizar y acceder a datos de manera rápida y eficiente. ¡Úsalos sabiamente! 🚀

