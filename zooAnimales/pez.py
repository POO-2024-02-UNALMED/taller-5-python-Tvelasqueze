from zooAnimales.animal import Animal

class Pez(Animal):
    lista=[]
    salmones=0
    bacalaos=0

    def __init__(self,nombre,edad,habitat,genero,color_escamas,cantidad_aletas):
        super().__init__(nombre,edad,habitat,genero)
        self.color_escamas=color_escamas
        self.cantidad_aletas=cantidad_aletas
        Pez.lista.append(self)

    @staticmethod
    def crearSalmon(nombre,edad,genero):
        Pez.salmones +=1
        return Pez(nombre,edad,"oceano",genero,"rojo",6)
    
    @staticmethod
    def crearBacalao(nombre,edad,genero):
        Pez.bacalaos +=1
        return Pez(nombre,edad,"oceano",genero,"gris",6)
    
    @staticmethod
    def cantidadPeces():
        return len(Pez.lista)
    
    def getColorEscamas(self):
        return self.color_escamas
    
    def getCantidadAletas(self):
        return self.cantidad_aletas
    
    def movimiento(self):
        return "nadar"