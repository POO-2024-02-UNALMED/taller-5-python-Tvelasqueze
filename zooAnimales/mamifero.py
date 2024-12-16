from zooAnimales.animal import Animal

class Mamifero(Animal):
    lista=[]
    leones=0
    caballos=0

    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self.pelaje=pelaje
        self.patas=patas
        Mamifero.lista.append(self)

    @staticmethod
    def crearLeon(nombre,edad,genero):
        Mamifero.leones +=1
        return Mamifero(nombre,edad,"selva",genero,True,4)
    
    @staticmethod
    def crearCaballo(nombre,edad,genero):
        Mamifero.caballos +=1
        return Mamifero(nombre,edad,"pradera",genero,True,4)
    
    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero.lista)
    
    def isPelaje(self):
        return self.pelaje
    
    def getPatas(self):
        return self.patas