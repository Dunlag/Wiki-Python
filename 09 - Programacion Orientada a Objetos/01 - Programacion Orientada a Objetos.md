## 📌 Introducción a la Programación Orientada a Objetos (POO)  

La **Programación Orientada a Objetos (POO)** es un paradigma de programación basado en la creación y manipulación de **objetos**, los cuales son instancias de **clases**.  

### 🔹 Conceptos Clave:  
- **Clase**: Es un molde o plantilla que define las características (atributos) y comportamientos (métodos) de un objeto.  
- **Objeto**: Es una instancia concreta de una clase.  
- **Atributos**: Variables que almacenan información dentro de una clase.  
- **Métodos**: Funciones definidas dentro de una clase que determinan su comportamiento.  

### 🔹 Ejemplo de una Clase y un Objeto:
```python
class Persona:
    def __init__(self, nombre, edad):  # Constructor de la clase
        self.nombre = nombre  # Atributo
        self.edad = edad  

    def saludar(self):  # Método de la clase
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Carlos", 25)
persona1.saludar()
```
**📌 Explicación:**  
- `__init__` es el **constructor** que se ejecuta automáticamente al crear un objeto.  
- `self` hace referencia a la instancia del objeto.  
- `persona1` es un **objeto** de la clase `Persona`.  

---

## 🔒 Encapsulamiento en la POO  

El **encapsulamiento** permite restringir el acceso a ciertos atributos y métodos de un objeto para proteger los datos.  

### 🔹 Modificadores de Acceso:
| Modificador | Uso en Python | Descripción |
|-------------|--------------|-------------|
| Público | `self.atributo` | Accesible desde cualquier parte. |
| Protegido | `_atributo` | Se **debe** tratar como privado, pero sigue accesible. |
| Privado | `__atributo` | No accesible directamente desde fuera de la clase. |

### 🔹 Ejemplo de Encapsulamiento:
```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular  # Público
        self._saldo = saldo  # Protegido
        self.__pin = "1234"  # Privado

    def ver_saldo(self):
        return f"Saldo disponible: {self._saldo}"

cuenta = CuentaBancaria("Ana", 5000)
print(cuenta.ver_saldo())  # ✅ Funciona
print(cuenta._saldo)  # ⚠️ Se puede acceder, pero no se recomienda
print(cuenta.__pin)  # ❌ Error, no se puede acceder directamente
```
**📌 Consejo:** Aunque los atributos con `_` y `__` pueden accederse de ciertas formas, lo ideal es **respetar el encapsulamiento** y usar métodos para interactuar con los datos.  

---

## 🔄 Herencia y Delegación  

La **herencia** permite que una clase (subclase) herede atributos y métodos de otra clase (superclase), promoviendo la reutilización de código.  

### 🔹 Ejemplo de Herencia:
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Hace un sonido"

class Perro(Animal):  # Perro hereda de Animal
    def hacer_sonido(self):
        return "Guau!"

perro1 = Perro("Bobby")
print(perro1.nombre)  # Hereda el atributo de Animal
print(perro1.hacer_sonido())  # Método sobreescrito en Perro
```
**📌 Consejo:** Si una subclase redefine un método de la superclase, se dice que **sobreescribe** el método.  

### 🔹 Delegación (`super()`)  
El método `super()` permite llamar a métodos de la superclase desde la subclase.  

```python
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)  # Llama al constructor de Animal
        self.color = color

gato1 = Gato("Michi", "Gris")
print(gato1.nombre, gato1.color)  # Usa atributos de ambas clases
```

---

## 🌀 Ejemplo Completo:  
```python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        return f"{self.marca} {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def describir(self):
        return f"{super().describir()} con {self.puertas} puertas"

mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.describir())
```

---

## 🚀 Resumen y Consejos Finales  
✅ Usa **clases** para estructurar mejor tu código.  
✅ **Encapsula** datos sensibles para evitar modificaciones no deseadas.  
✅ Aprovecha la **herencia** para reutilizar código.  
✅ Usa `super()` para **delegar** comportamientos a la superclase.  
✅ Recuerda que **Python permite herencia múltiple**, pero úsala con cuidado para evitar problemas de ambigüedad.  

---
