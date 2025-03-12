# Listas en Python

Las listas en Python son estructuras de datos que permiten almacenar múltiples elementos en un solo objeto. Son mutables, lo que significa que se pueden modificar después de su creación.

## Creación y tipos de listas

```python
lista1 = []  # Lista vacía
print(type(lista1))

lista2 = [1, "a", True]  # Lista con diferentes tipos de datos
```

## Recorrido de una lista

Podemos recorrer una lista con un bucle `for`:

```python
lista = [1, 2, 3, 4, 5, 6]
for num in lista:
    print(num)
```

Podemos recorrer dos listas a la vez usando `zip`:

```python
lista2 = ["a", "b", "c", "d", "e"]
for num, letra in zip(lista, lista2):
    print(num, " ", letra)
```

## Operaciones con listas

- Comprobar si un elemento está en la lista:

```python
7 in lista  # False
```

- Concatenar listas:

```python
lista + [6, 7, 8]
```

- Slicing (rebanado):

```python
lista[2:4]      # Elementos desde la posición 2 a la 3
lista[2:5:2]    # Elementos desde la posición 2 a la 4 con saltos de 2
lista[::-1]     # Lista en orden inverso
```

- Funciones útiles:

```python
max(lista)  # Mayor valor de la lista
min(lista)  # Menor valor de la lista
sum(lista)  # Suma de los elementos
```

## Ordenar listas

```python
lista = [3, 7, 1, 9, 12, 34, 0]
sorted(lista)  # Orden ascendente
sorted(lista, reverse=True)  # Orden descendente
```

## Listas anidadas

Podemos crear listas dentro de listas:

```python
tabla = [[1, 2, 3], [4, 5, 6]]
for fila in tabla:
    for elem in fila:
        print(elem)
```

## Mutabilidad de las listas

Las listas pueden modificarse después de su creación:

```python
lista5 = [1, 2, 3]        
lista5[1] = 100  # Modifica el segundo elemento
print(lista5)  # [1, 100, 3]
```

### Copia de listas

Si asignamos una lista a otra variable, ambas apuntan al mismo objeto:

```python
lista5.append(5)
lista6 = lista5
lista5.append(100)
print(lista6)  # [1, 100, 3, 5, 100]
```

Para hacer una copia independiente:

```python
lista7 = lista6[:]
print(lista7)  # [1, 100, 3, 5]
lista6.append(44)
print(lista6)  # [1, 100, 3, 5, 100, 44]
print(lista7)  # [1, 100, 3, 5, 100]
```

## Métodos principales de listas

```python
lista = [1, 2, 3]
lista.append(4)  # Agrega un elemento al final

lista2 = [5, 6]
lista.extend(lista2)  # Extiende la lista con otra lista

lista.insert(1, 100)  # Inserta 100 en la posición 1

lista.pop()  # Elimina el último elemento
lista.pop(1)  # Elimina el elemento en la posición 1

lista.remove(3)  # Elimina la primera ocurrencia de 3

lista.reverse()  # Invierte el orden de la lista

lista.sort()  # Ordena la lista en orden ascendente
lista.sort(reverse=True)  # Ordena en orden descendente

lista.count(5)  # Cuenta cuántas veces aparece el número 5
lista.index(5)  # Devuelve la posición de la primera ocurrencia de 5
```

## Consejos y tips 📌

✅ **Usa listas para almacenar múltiples elementos sin necesidad de variables adicionales.**  
✅ **Si necesitas recorrer una lista mientras mantienes un índice, usa `enumerate()`.**  
✅ **Para evitar modificar la lista original al hacer copias, usa `lista[:]` o `lista.copy()`.**  
✅ **Cuando trabajes con listas anidadas, usa comprensión de listas para mejorar el rendimiento.**  
✅ **Si solo necesitas ordenar temporalmente sin modificar la lista original, usa `sorted(lista)`.**  

---


