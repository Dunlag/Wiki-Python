import math
class Punto():
    #Representacion de un punto en un plano
    #donde los atributos representan los valores de coordenadas
    
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        
    def mostrar(self):
        return str(self.x)+":"+str(self.y)
    
    def distancia(self, otro):
        """Devuelve la distancia entre ambos puntos"""
        dx = self.x - otro.x 
        dy = self.y - otro.y 
        return math.sqrt((dx*dx + dy*dy))