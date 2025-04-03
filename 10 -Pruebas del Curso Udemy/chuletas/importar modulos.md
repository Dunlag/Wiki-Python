# 📦 Cheatsheet: Imported Modules en Python

## 🔹 ¿Qué son los módulos y bibliotecas en Python?

- **Builtin objects**: Son objetos escritos en C dentro del intérprete de Python.
- **Builtin modules**: Son módulos que contienen objetos integrados en Python.
- **Standard libraries**: Incluyen módulos escritos en C y en Python.
- **Packages**: Son colecciones de módulos `.py`.
- **Third-party libraries**: Módulos creados por terceros (no por el equipo de desarrollo de Python).

---

## 📥 Importando módulos en Python

Algunos objetos no están disponibles directamente en el **namespace global** y necesitan ser importados antes de usarse.

Ejemplo de uso del módulo `time`:

```python
import time
time.sleep(5)  # Pausa la ejecución por 5 segundos
```

---

## 📜 Listar todos los módulos incorporados

Puedes obtener una lista de los módulos **incorporados en Python** con:

```python
import sys
print(sys.builtin_module_names)
```

---

## 📌 Ubicación de las bibliotecas estándar

Las bibliotecas estándar escritas en Python se encuentran en la carpeta de instalación de Python. Para ver la ruta, usa:

```python
import sys
print(sys.prefix)
```

---

## 📦 Instalación de bibliotecas de terceros

Los módulos de terceros no vienen con Python y deben instalarse manualmente.

### 🖥️ En Windows:

```sh
pip install pandas
```

Si no funciona, prueba:

```sh
python -m pip install pandas
```

### 🍏🐧 En macOS y Linux:

```sh
pip3 install pandas
```

Si hay problemas, usa:

```sh
python3 -m pip install pandas
```

---
