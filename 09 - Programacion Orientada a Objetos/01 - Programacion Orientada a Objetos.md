## 📌 Introducción a la Programación Orientada a Objetos (POO)  

La **POO** organiza el código en **clases** y **objetos**, permitiendo una mejor estructuración y reutilización del código.  

### 🔹 Conceptos Clave:  
- **Clase**: Define un conjunto de atributos y métodos.  
- **Objeto**: Instancia concreta de una clase.  
- **Atributos**: Variables asociadas a un objeto.  
- **Métodos**: Funciones dentro de una clase que definen su comportamiento.  

---

## 🎯 Creación de una Clase: `Punto`  

```python
import math

class Punto():
    """Representación de un punto en un plano cartesiano"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mostrar(self):
        """Devuelve las coordenadas como una cadena"""
        return str(self.x) + ":" + str(self.y)

    def distancia(self, otro):
        """Calcula la distancia entre dos puntos"""
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt((dx * dx) + (dy * dy))
```

**📌 Explicación:**  
- `__init__`: Constructor que inicializa `x` e `y`.  
- `mostrar()`: Devuelve las coordenadas en formato `x:y`.  
- `distancia(otro)`: Calcula la distancia entre dos puntos.  

---

## ⚙️ Uso de la Clase `Punto`  

```python
>>> from puntos import Punto
>>> punto1 = Punto()  # Se crea un punto en (0,0)
>>> punto1.x
0
>>> punto1.y
0
>>> punto1.y = 5  # Se cambia el valor de y
>>> punto1.mostrar()
'0:5'
```

✅ **Los atributos pueden modificarse directamente**.  

```python
>>> punto1.distancia()
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    punto1.distancia()
TypeError: Punto.distancia() missing 1 required positional argument: 'otro'
```
❌ **Error**: Se debe pasar otro punto como argumento.  

```python
>>> punto2 = Punto(8,9)  # Se crea un segundo punto en (8,9)
>>> punto1.distancia(punto2)
8.9442719
```
✅ **Ahora sí funciona porque se ha proporcionado otro punto**.  

---

## 🔒 Encapsulamiento  

Aunque en este ejemplo no hay atributos privados, podemos usar `__atributo` para hacer que no sean accesibles directamente:  

```python
class Punto():
    def __init__(self, x=0, y=0):
        self.__x = x  # Privado
        self.__y = y  # Privado
```
Esto impide el acceso directo:  
```python
>>> punto1 = Punto(3,4)
>>> print(punto1.__x)
AttributeError: 'Punto' object has no attribute '__x'
```
**📌 Consejo:** Usa **métodos** en lugar de acceder directamente a atributos privados.  

---

## 🔄 Herencia  

Podemos crear una subclase `Punto3D` que herede de `Punto`:  

```python
class Punto3D(Punto):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def mostrar(self):
        return f"{self.x}:{self.y}:{self.z}"
```

```python
>>> punto3d = Punto3D(1,2,3)
>>> punto3d.mostrar()
'1:2:3'
```

---

## 🌀 Resumen y Consejos  

✅ **Usa clases** para organizar el código.  
✅ **Encapsula** atributos sensibles con `__`.  
✅ **Hereda** para reutilizar código.  
✅ **Pasa correctamente los parámetros** para evitar errores.  
