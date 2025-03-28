Aquí tienes tu cheatsheet bien maquetada en Markdown para tu repositorio:  

```markdown
# 📜 Cheatsheet: Operations with Data Types

## 📌 Índices en Listas, Cadenas y Tuplas

Estos tipos de datos tienen un **sistema de índices positivo**:

```plaintext
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
```

Y también un **sistema de índices negativo**:

```plaintext
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
```

---

## ✂️ Slicing (Segmentación) en Listas

### 📌 Obtener los elementos 2º, 3º y 4º:
```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[1:4])  
# Output: ['Tue', 'Wed', 'Thu']
```

### 📌 Obtener los tres primeros elementos:
```python
print(days[:3])  
# Output: ['Mon', 'Tue', 'Wed']
```

### 📌 Obtener los tres últimos elementos:
```python
print(days[-3:])  
# Output: ['Fri', 'Sat', 'Sun']
```

### 📌 Obtener todo excepto el último:
```python
print(days[:-1])  
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
```

### 📌 Obtener todo excepto los dos últimos:
```python
print(days[:-2])  
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
```

---

## 🔑 Acceso a Valores en Diccionarios

Se accede a los valores de un diccionario usando su clave correspondiente:

```python
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
print(phone_numbers["Marry"])  
# Output: '+423998200919'
```

---

📌 **Consejo:** El slicing (`[:]`) es una forma poderosa de manipular listas en Python. 🚀
```

Este formato es claro, estructurado y fácil de leer en tu repositorio. ¡Listo para copiar y pegar! 🎯