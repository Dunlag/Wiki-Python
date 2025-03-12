# Métodos de las Cadenas de Caracteres en Python

Las cadenas de caracteres en Python son secuencias inmutables de caracteres que permiten diversas operaciones y métodos para su manipulación.

## Recorrer una cadena carácter por carácter
Puedes recorrer una cadena utilizando un bucle `for`:
```python
cadena = "informatica"
for c in cadena:
    print(c)
```

## Operadores `in` y `not in`
Puedes comprobar si un carácter o una subcadena está dentro de una cadena:
```python
"a" in cadena  # True
"b" in cadena  # False
"a" not in cadena  # False
```

## Acceder a caracteres específicos
```python
cadena[0]      # 'i'
cadena[2:5]    # 'for'
cadena[2:7:2]  # 'fot'
cadena[::-1]   # 'acitamrofni' (inversión de la cadena)
```

## Inmutabilidad de las cadenas
Las cadenas de caracteres en Python son **inmutables**, lo que significa que no se pueden modificar después de ser creadas:
```python
cadena[2] = "g"  # Error: TypeError: 'str' object does not support item assignment
```
Para modificar una cadena, debes crear una nueva:
```python
cadena = cadena.upper()  # Transforma toda la cadena a mayúsculas
```

## Métodos principales de cadenas
Python ofrece varios métodos útiles para trabajar con cadenas.

### Modificación de formato
```python
cad = "hola, como estas?"
cad.capitalize()  # 'Hola, como estas?'

cad = "hola mundo"
cad.upper()       # 'HOLA MUNDO'
cad.lower()       # 'hola mundo'
cad.swapcase()    # 'HOLA MUNDO' -> 'hola mundo' y viceversa
cad.title()       # 'Hola Mundo'
```

### Contar ocurrencias de caracteres o subcadenas
```python
cad = "bienvenido a mi aplicacion"
cad.count("a")        # 3 (cantidad de 'a' en toda la cadena)
cad.count("a", 16)    # 1 (cantidad de 'a' desde la posición 16)
cad.count("a", 10, 16) # 1 (entre las posiciones 10 y 16)
```

### Búsqueda de subcadenas
```python
cad.find("mi")    # 12 (posición de la primera aparición de 'mi')
cad.find("hola")  # -1 (no encontrado)
```

### Comprobar prefijos y sufijos
```python
cad.startswith("b")         # True (empieza con 'b')
cad.startswith("bien", 13)  # False (desde la posición 13 no empieza con 'bien')
cad.endswith("cion")        # True (termina en 'cion')
```

### Reemplazo de caracteres
```python
cad.replace("a", "U")  # Reemplaza todas las 'a' por 'U'
```

### Eliminar espacios en blanco
```python
cad = "   bienvenido a mi aplicacion   "
cad.strip()  # 'bienvenido a mi aplicacion' (elimina espacios al inicio y final)
```

### División de cadenas
```python
hora = "12:23:12"
hora.split(":")  # ['12', '23', '12']
```

## Consejos y buenas prácticas
- Usa `strip()` para limpiar datos de entrada de usuarios.
- `split()` es muy útil para trabajar con datos estructurados (CSV, logs, etc.).
- `find()` y `count()` son útiles para validar entradas de usuario.
- Usa `replace()` para hacer modificaciones rápidas en textos.

Estos métodos te ayudarán a manejar y manipular cadenas de manera eficiente en Python. 🚀

