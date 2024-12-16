from typing import List

class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self):
        total = 0
        for zona in self.zonas:
            total += zona.cantidadAnimales()
        return total
    
    def getNombre(self):
        return self.nombre
    
    def getZona(self):
        return self.zonas