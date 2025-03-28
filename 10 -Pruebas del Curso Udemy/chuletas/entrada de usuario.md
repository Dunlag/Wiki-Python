Aquí tienes la chuleta bien maquetada en Markdown para tu repositorio:  

```markdown
# 📝 Cheatsheet: Processing User Input

## 🖥️ Obtener Entrada del Usuario

En Python, puedes obtener datos del usuario con la función `input()`:

```python
name = input("Enter your name: ")
```

🔹 La ejecución del programa se detiene hasta que el usuario ingresa un valor.

---

## 🔄 Convertir Entrada de Usuario

Por defecto, `input()` devuelve una cadena (`str`). Puedes convertirla a otros tipos de datos:

```python
experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
```

---

## 🎨 Formatear Cadenas de Texto

Puedes usar `.format()` para insertar valores en una cadena:

```python
name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
```

**Salida:**
```
Hi Sim, you have 1.5 years of experience.
```

📌 **Consejo:** También puedes usar f-strings (Python 3.6+):

```python
print(f"Hi {name}, you have {experience_years} years of experience.")
```

---

🚀 **Tip Extra:** Usa `float()` en lugar de `int()` si esperas valores con decimales:

```python
experience_years = float(experience_months) / 12
```
```

Este formato hace que la información sea más clara, visualmente atractiva y fácil de leer en tu repositorio. ¡Listo para copiar y pegar! 🚀