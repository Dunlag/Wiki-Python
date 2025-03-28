# 🔄 Tip: Converting Between Datatypes

A veces es necesario convertir entre diferentes tipos de datos en Python. Esto es muy fácil de hacer:

## 🔄 De tupla a lista:
```python
cool_tuple = (1, 2, 3)
cool_list = list(cool_tuple)
print(cool_list)  
# Output: [1, 2, 3]
```

## 🔄 De lista a tupla:
```python
cool_list = [1, 2, 3]
cool_tuple = tuple(cool_list)
print(cool_tuple)  
# Output: (1, 2, 3)
```

## 🔄 De cadena a lista:
```python
cool_string = "Hello"
cool_list = list(cool_string)
print(cool_list)  
# Output: ['H', 'e', 'l', 'l', 'o']
```

## 🔄 De lista a cadena:
```python
cool_list = ['H', 'e', 'l', 'l', 'o']
cool_string = "".join(cool_list)
print(cool_string)  
# Output: 'Hello'
```

### ℹ️ Nota:
Convertir una lista en una cadena requiere `str.join()`, ya que `str()` por sí solo no es suficiente.

Prueba el siguiente código para entender mejor cómo funciona `str.join()`:
```python
cool_list = ['H', 'e', 'l', 'l', 'o']
cool_string = "---".join(cool_list)
print(cool_string)  
# Output: 'H---e---l---l---o'
```
Aquí, `"---"` se usa como separador entre cada elemento de la lista. 🚀
```