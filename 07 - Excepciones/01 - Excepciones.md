# Manejo de Excepciones en Python

El manejo de excepciones en Python permite controlar errores en la ejecución de un programa y evitar que este termine abruptamente. Para ello, se utilizan las estructuras `try`, `except`, `else` y `finally`.

## Bloques de Excepción en Python

### 1. `try` y `except`
El bloque `try` contiene el código que puede generar una excepción. Si ocurre un error, el control pasa al bloque `except`, donde se maneja la excepción.

Ejemplo:
```python
while True:
    try:
        x = int(input("Dime un numero: "))
        break
    except ValueError:
        print("Debes introducir un numero")
```
**Explicación:**
- Se solicita al usuario un número.
- Si el usuario ingresa un valor que no es un número entero, se captura la excepción `ValueError` y se muestra un mensaje de error en pantalla.
- El bucle sigue ejecutándose hasta que el usuario ingrese un valor válido.

### 2. `else`
El bloque `else` se ejecuta solo si el código dentro de `try` no genera una excepción.

Ejemplo:
```python
try:
    x = int(input("Dime un numero: "))
except ValueError:
    print("Debes introducir un numero")
else:
    print("Número introducido correctamente")
```
**Explicación:**
- Si el usuario introduce un número válido, se ejecuta el `else`.
- Si ocurre una excepción, el bloque `except` maneja el error y `else` no se ejecuta.

### 3. `finally`
El bloque `finally` se ejecuta siempre, haya ocurrido una excepción o no.

Ejemplo:
```python
try:
    x = int(input("Dime un numero: "))
except ValueError:
    print("Debes introducir un numero")
finally:
    print("Se ha finalizado el programa")
```
**Explicación:**
- `finally` se ejecutará siempre, sin importar si hubo un error o no.
- Es útil para liberar recursos o realizar acciones que deben ejecutarse al final del proceso.

## Consejos y Buenas Prácticas
✔️ Usa excepciones solo cuando sea necesario; no abuses de `try-except` para controlar el flujo del programa.
✔️ Captura excepciones específicas en lugar de usar un `except` genérico.
✔️ Utiliza `finally` para liberar recursos, cerrar archivos o conexiones a bases de datos.
✔️ Evita capturar excepciones sin manejarlas, ya que esto puede ocultar errores importantes.
✔️ Si necesitas definir excepciones personalizadas, puedes crear clases que hereden de `Exception`.

Ejemplo de excepción personalizada:
```python
class NumeroNegativoError(Exception):
    pass

try:
    num = int(input("Introduce un número positivo: "))
    if num < 0:
        raise NumeroNegativoError("No se permiten números negativos.")
except NumeroNegativoError as e:
    print(e)
```

