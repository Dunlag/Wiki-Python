# Estructuras de Control en Python

Las estructuras de control permiten tomar decisiones en el flujo de ejecución de un programa. En Python, las más utilizadas son `if`, `if-else`, `if-elif-else` y, aunque Python no tiene `switch` nativo, se pueden usar diccionarios para simularlo.

---
## 1. Condicional `if`
La estructura `if` permite ejecutar un bloque de código si se cumple una condición.

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
```

### 🔹 Consejos:
- La indentación es clave en Python. Asegúrate de usar espacios o tabulaciones de manera consistente.
- La condición debe evaluarse como `True` para que el bloque de código dentro del `if` se ejecute.

---
## 2. Condicional `if-else`
El `if-else` nos permite definir una acción alternativa si la condición no se cumple.

```python
edad = int(input("Introduce tu edad: "))
if edad >= 18:
    print("Puedes entrar al club.")
else:
    print("No puedes entrar, eres menor de edad.")
```

### 🔹 Consejos:
- `else` no lleva condición; simplemente se ejecuta si el `if` es `False`.
- Es útil para manejar diferentes escenarios en una decisión.

---
## 3. Condicional `if-elif-else`
Si tenemos múltiples condiciones, podemos usar `elif` (abreviatura de *else if*).

```python
calificacion = int(input("Introduce tu nota: "))

if calificacion >= 90:
    print("Tienes una A")
elif calificacion >= 80:
    print("Tienes una B")
elif calificacion >= 70:
    print("Tienes una C")
elif calificacion >= 60:
    print("Tienes una D")
else:
    print("Has reprobado")
```

### 🔹 Consejos:
- `elif` permite evaluar varias condiciones en orden.
- Solo se ejecutará el primer `if` o `elif` que sea `True`.

---
## 4. Simulación de `switch-case` en Python
Python no tiene `switch-case`, pero se puede simular con diccionarios.

```python
def dias_semana(numero):
    switch = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return switch.get(numero, "Día inválido")

print(dias_semana(3))  # Output: Miércoles
```

### 🔹 Consejos:
- Se usa un diccionario donde las claves son los valores a comparar y los valores son las respuestas.
- `get()` permite definir un valor por defecto si la clave no existe (similar a un `default` en `switch`).

---
## 🌟 Resumen
- `if` ejecuta código si la condición es `True`.
- `if-else` proporciona una alternativa cuando la condición es `False`.
- `if-elif-else` permite múltiples condiciones encadenadas.
- No hay `switch`, pero se puede simular con diccionarios.


