# Introducción a Python 3

Python es un lenguaje de programación fácil de aprender y ampliamente utilizado en diversos campos como el desarrollo web, ciencia de datos, inteligencia artificial, entre otros. En esta guía, aprenderás a ejecutar programas en Python desde la terminal y desde archivos.

---

## Ejecutar Python desde la terminal

Para ejecutar Python directamente desde la terminal, abre un terminal y escribe:

```bash
python3
```

Esto abrirá el **intérprete interactivo** de Python, donde puedes escribir código línea por línea y ejecutarlo en tiempo real.

Ejemplo:

```python
>>> print("Hola mundo")
Hola mundo
```

Para salir del intérprete, usa:

```bash
exit()
```

o presiona `Ctrl + D` en Linux/macOS o `Ctrl + Z` en Windows y luego `Enter`.

---

## Ejecutar un archivo Python

Si tienes un archivo `script.py` con el siguiente contenido:

```python
print("Hola mundo")
```

Puedes ejecutarlo en la terminal con:

```bash
python3 script.py
```

Esto imprimirá `Hola mundo` en la terminal.

---

## Estructura básica de un programa en Python

Python permite interactuar con el usuario y tomar decisiones. Veamos un programa básico que pide la edad y determina si eres mayor de edad:

```python
# Programa que pide la edad y dice si eres mayor de edad
edad = int(input("Dime tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
print("Programa terminado")
```

Ejemplo de ejecución:

```
Dime tu edad: 20
Eres mayor de edad
Programa terminado
```

---

## Consejos y Tips

- Usa `python3 -i script.py` para ejecutar un script y luego quedarte en el modo interactivo.
- Agrega `#!/usr/bin/env python3` al inicio de un script para ejecutarlo como un programa independiente en Linux/macOS.
- Usa `print()` para depurar valores de variables rápidamente.

---


