from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas=0
    salamandras=0
    lista=[]

    def __init__(self, nombre, edad, habitat, genero, color_piel,venenoso):
        super().__init__(nombre, edad, habitat,genero)
        self.color_piel=color_piel
        self.venenoso=venenoso
        Anfibio.lista.append(self)
        
    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas+=1
        return Anfibio(nombre,edad,"selva",genero,"rojo", True)
    
    @staticmethod
    def crearSalamandra(nombre,edad,genero):
        Anfibio.salamandras+=1
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)

    @staticmethod
    def CantidadAnfibios():
        return len(Anfibio.Lista)
    
    def movimiento(self):
        return "saltar"
    
    def getColorPiel(self):
        return self.color_piel

    def isVenenoso(self):
        return self.venenoso