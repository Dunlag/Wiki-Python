# Estructuras de Control en Python

## La sentencia `while`

En Python, la estructura de control `while` permite ejecutar un bloque de código repetidamente mientras se cumpla una condición.

### Sintaxis básica:
```python
while condicion:
    # Código que se ejecuta mientras la condición sea verdadera
```

### Ejemplo: Solicitar una clave con `while`
```python
secreto = "hola"
clave = input("Dime la clave: ")
while clave != secreto:
    print("Clave incorrecta!")
    retry = input("¿Quieres volver a intentarlo? (S/N): ")
    if retry.upper() == "N":
        break  # Sale del bucle si el usuario no quiere seguir intentándolo
    clave = input("Dime la clave: ")
if clave == secreto:
    print("Bienvenido")
print("Programa terminado")
```

### Uso de `break`
La sentencia `break` se utiliza para salir completamente del bucle sin esperar a que la condición se haga falsa. 

✅ **Consejo:** Úsalo con cuidado para evitar salir del bucle de forma inesperada.

---

### Uso de `continue`
La sentencia `continue` permite saltar el resto del código en la iteración actual y pasar a la siguiente.

### Ejemplo: Imprimir solo los números pares del 1 al 10
```python
cont = 0 
while cont < 10:
    cont = cont + 1
    if cont % 2 == 1:
        continue  # Salta la impresión si el número es impar
    print(cont)
```

🔹 En este caso, cuando `cont` es impar, `continue` hace que la impresión se salte y el bucle siga con la siguiente iteración.

---

## ¿Por qué Python no tiene `do-while`?

En muchos lenguajes de programación existe la estructura `do-while`, que ejecuta el bloque al menos una vez antes de comprobar la condición. Python no tiene esta estructura de manera nativa, pero se puede simular con un `while` de la siguiente manera:

### Simulación de `do-while` en Python:
```python
while True:
    dato = input("Introduce un número positivo: ")
    if int(dato) > 0:
        break  # Sale del bucle si el número es positivo
    print("Número no válido, intenta otra vez.")
```

Aquí el código se ejecuta al menos una vez, similar a un `do-while` en otros lenguajes.

🔹 **Consejo:** Aunque Python no tenga `do-while`, puedes lograr el mismo efecto usando `while True` y `break` de manera adecuada.

---

✅ **Resumen de conceptos clave:**
- `while` repite un bloque de código mientras la condición sea verdadera.
- `break` termina el bucle inmediatamente.
- `continue` salta el resto del código en una iteración y pasa a la siguiente.
- Python no tiene `do-while`, pero se puede simular con `while True` y `break`.

---


