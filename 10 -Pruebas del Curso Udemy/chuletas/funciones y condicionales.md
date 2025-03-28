# 📜 Cheatsheet: Functions and Conditionals

## 📌 Definir Funciones

En Python, una función se define con `def`:

```python
def cube_volume(a):
    return a * a * a
```

---

## ⚡ Estructuras Condicionales

### 📌 If-Else

```python
message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")
```

### 📌 If-Elif-Else

```python
message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
```

---

## 🔀 Operadores Lógicos

### 📌 `and` (Ambas condiciones deben ser `True`)

```python
x = 1
y = 1
 
if x == 1 and y == 1:
    print("Yes")
else:
    print("No")
```

### 📌 `or` (Al menos una condición debe ser `True`)

```python
x = 1
y = 2
 
if x == 1 or y == 2:
    print("Yes")
else:
    print("No")
```

---

## 🔍 Comprobar Tipos de Datos

### 📌 Usando `isinstance()`
```python
print(isinstance("abc", str))    # True
print(isinstance([1, 2, 3], list)) # True
```

### 📌 Usando `type()`
```python
print(type("abc") == str)    # True
print(type([1, 2, 3]) == list) # True
```

---

📌 **Consejo:** Usa `isinstance()` en lugar de `type()` cuando necesites comprobar tipos en herencia de clases. 🚀
```