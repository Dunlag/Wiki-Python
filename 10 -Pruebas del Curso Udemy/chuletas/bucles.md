# 🔄 Cheatsheet: Loops en Python

## 🔁 For-Loops

Los `for`-loops permiten ejecutar un bloque de código repetidamente.

### 🔡 Iterar sobre una cadena

```python
for letter in 'abc':
    print(letter.upper())
```

**Salida:**
```
A
B
C
```

📌 **Nota:** `letter` es solo un nombre de variable que representa cada elemento de la iteración.

---

### 📖 Iterar sobre las claves de un diccionario

```python
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key in phone_numbers.keys():
    print(key)
```

**Salida:**
```
John Smith
Marry Simpons
```

---

### 🔢 Iterar sobre los valores de un diccionario

```python
for value in phone_numbers.values():
    print(value)
```

**Salida:**
```
+37682929928
+423998200919
```

---

### 🗂️ Iterar sobre los pares clave-valor de un diccionario

```python
for key, value in phone_numbers.items():
    print(key, value)
```

**Salida:**
```
John Smith +37682929928
Marry Simpons +423998200919
```

---

## 🔄 While-Loops

Los `while`-loops ejecutan un bloque de código mientras una condición sea `True`.

```python
import datetime

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
```

📌 **Nota:** Este bucle imprimirá el mensaje hasta que la fecha y hora sean las especificadas.

---

✅ **Consejo:**  
Si necesitas salir de un `while`-loop antes de que la condición sea falsa, usa `break`.

```python
x = 0
while x < 5:
    print(x)
    x += 1
    if x == 3:
        break
```

Esto imprimirá:
```
0
1
2
```

---

