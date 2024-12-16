from zooAnimales.animal import Animal

class Reptil(Animal):
    lista=[]
    iguanas=0
    serpientes=0

    def __init__(self,nombre,edad,habitat,genero,color_escamas,largo_cola):
        super().__init__(nombre,edad,habitat,genero)
        self.color_escamas=color_escamas
        self.largo_cola=largo_cola
        Reptil.lista.append(self)

    @staticmethod
    def crearIguana(nombre,edad,genero):
        Reptil.iguanas +=1
        return Reptil(nombre,edad,"humedal",genero,"verde",3)
    
    @staticmethod
    def crearSerpiente(nombre,edad,genero):
        Reptil.serpientes +=1
        return Reptil(nombre,edad,"jungla",genero,"blanco",1)
    
    @staticmethod
    def cantidadReptiles():
        return len(Reptil.lista)
    
    def movimiento(self):
        return "reptar"
    
    def getColorEscamas(self):
        return self.color_escamas
    
    def getLargoCola(self):
        return self.largo_cola