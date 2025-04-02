# 📂 Cheatsheet: File Processing en Python

## 📖 Leer un archivo existente

Para leer un archivo en Python, usa `open()` en modo lectura (`r` por defecto).

```python
with open("file.txt") as file:
    content = file.read()
```

---

## ✍️ Crear y escribir en un archivo

Si el archivo no existe, se creará. Si ya existe, **su contenido será sobrescrito**.

```python
with open("file.txt", "w") as file:
    file.write("Sample text")
```

📌 **Nota:** Usa `"w"` solo si estás seguro de que quieres borrar el contenido anterior.

---

## ➕ Agregar texto sin sobrescribir

Para **añadir** texto a un archivo sin borrar su contenido, usa el modo `"a"` (append).

```python
with open("file.txt", "a") as file:
    file.write("More sample text")
```

📌 **Nota:** El texto se añadirá al final del archivo.

---

## 🔄 Leer y agregar texto en un archivo

Si necesitas **leer y agregar** contenido al mismo tiempo, usa el modo `"a+"`.

```python
with open("file.txt", "a+") as file:
    file.write("Even more sample text")
    file.seek(0)  # Mueve el cursor al inicio del archivo
    content = file.read()
```

📌 **Explicación:**
- `"a+"` permite escribir **y** leer en el archivo.
- `file.seek(0)` mueve el cursor al inicio para poder leer el contenido.

---
