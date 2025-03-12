# Guía sobre Tuplas en Python

## ¿Qué es una tupla?
Las tuplas en Python son estructuras de datos similares a las listas, pero con una diferencia clave: **son inmutables**. Esto significa que una vez creadas, no se pueden modificar (ni agregar ni eliminar elementos).

### Definición de tuplas
Se pueden definir de varias formas:

```python
# Tupla vacía
tupla1 = ()

# Tupla con diferentes tipos de datos
tupla2 = ("a", 1, True)

# Tupla con números
tupla = (1, 2, 3)
```

### Acceder a elementos de una tupla
Los elementos de una tupla se acceden por su índice, igual que en una lista:

```python
print(tupla[0])  # Devuelve 1
print(tupla[0:1])  # Devuelve (1,)
print(len(tupla))  # Devuelve 3
```

### Importante: Las tuplas son inmutables
Una vez creada una tupla, no podemos modificar sus elementos:

```python
tupla[1] = 6  # Esto genera un TypeError
```

## Operaciones con Tuplas
### Desempaquetado de tuplas
Podemos asignar los valores de una tupla a variables:

```python
divmod(7, 2)  # Devuelve (3, 1)

# Desempaquetado
cociente, resto = divmod(7, 2)
print(cociente)  # Devuelve 3
print(resto)  # Devuelve 1
```

### Funciones con tuplas
Algunas funciones incorporadas que funcionan con tuplas:

```python
tupla = (4, 8, 1, 9)
print(max(tupla))  # Devuelve 9
print(min(tupla))  # Devuelve 1
print(len(tupla))  # Devuelve 4
```

### Convertir entre listas y tuplas
A veces puede ser útil convertir entre listas y tuplas:

```python
lista = [1, 2, 3]
tupla = tuple(lista)  # Convierte la lista en una tupla
print(tupla)  # Devuelve (1, 2, 3)

nueva_lista = list(tupla)  # Convierte la tupla en una lista
print(nueva_lista)  # Devuelve [1, 2, 3]
```

## Tips y Consejos
✅ Usa tuplas cuando los datos no necesiten modificarse. Son más eficientes que las listas en términos de memoria y rendimiento.

✅ Pueden servir para representar datos estructurados, como coordenadas o registros en bases de datos.

✅ Si necesitas modificar la tupla, conviértela en lista, haz los cambios y luego vuelve a convertirla en tupla.

---

Con esta guía tienes una base sólida sobre las tuplas en Python. 🚀 Si tienes dudas, ¡prueba los ejemplos en tu terminal! 😃

