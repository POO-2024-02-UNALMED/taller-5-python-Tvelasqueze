from typing import List
from gestion.zoologico import Zoologico
from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre,zoo):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def cantidadAnimales(self):
        return len(self.animales)
    
    def getZoo(self):
        return self.zoo
    
    def getNombre(self):
        return self.nombre