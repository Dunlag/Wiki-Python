

# 📌 Instalación de Python 3 en Linux y Windows

Python 3 es un lenguaje de programación versátil y ampliamente utilizado. A continuación, explico cómo instalarlo en Linux y Windows.



## 🐧 Instalación en Linux  

En la mayoría de las distribuciones de Linux, Python ya viene preinstalado. Para verificarlo, abre la terminal y ejecuta:

```bash
python3 --version
```

Si tienes Python 3 instalado, verás algo como:

```
Python 3.x.x
```

Si no está instalado o necesitas actualizarlo, sigue estos pasos:

### 🔹 Ubuntu / Debian  
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
```

### 🔹 Arch Linux (y derivadas como Manjaro)  
```bash
sudo pacman -Syu python python-pip
```

### 🔹 Fedora  
```bash
sudo dnf install python3 python3-pip -y
```

**📌 Consejo:**  
Después de instalar Python, asegúrate de que `pip`, el gestor de paquetes de Python, esté actualizado con:  

```bash
pip3 install --upgrade pip
```

---

## 🖥 Instalación en Windows  

1. Descarga el instalador desde la web oficial de Python:  
   👉 [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

2. **Ejecuta el instalador** (`python-3.x.x.exe`) y marca la opción **"Add Python to PATH"** antes de continuar. Esto evitará problemas al ejecutar Python desde la terminal.

3. Haz clic en **"Install Now"** y espera a que finalice la instalación.

4. Verifica la instalación abriendo la terminal de Windows (PowerShell o CMD) y escribiendo:

   ```powershell
   python --version
   ```

   Debería mostrar algo como:

   ```
   Python 3.x.x
   ```

**📌 Consejos útiles:**  
✔️ Si olvidaste marcar "Add Python to PATH", puedes solucionarlo manualmente agregando la ruta de Python a las variables de entorno.  
✔️ Usa **Windows Terminal** en lugar del CMD para una mejor experiencia de línea de comandos.  
✔️ Considera instalar **WSL (Windows Subsystem for Linux)** si prefieres trabajar con Python en un entorno más similar a Linux.  

---

## 🎯 Comprobación final  

Después de la instalación, puedes probar Python ejecutando el siguiente comando en la terminal:

```bash
python3
```
O en Windows (según la versión instalada):

```powershell
python
```

Debería abrirse el intérprete interactivo de Python, donde puedes escribir código directamente. Para salir, usa:

```python
exit()
```

¡Listo! Ya tienes Python 3 instalado y funcionando. 🚀  

---
