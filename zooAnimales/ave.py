from zooAnimales.animal import Animal

class Ave(Animal):
    lista=[]
    halcones=0
    aguilas=0

    def __init__(self,nombre,edad,habitat,genero,color_plumas):
        super().__init__(nombre,edad,habitat,genero)
        self.color_plumas=color_plumas
        Ave.lista.append(self)

    @staticmethod
    def crearHalcon(nombre,edad,genero):
        Ave.halcones +=1
        return Ave(nombre,edad,"montañas",genero,"cafe glorioso")
    
    @staticmethod
    def crearAguila(nombre,edad,genero):
        Ave.aguilas += 1
        return Ave(nombre,edad,"montañas",genero,"blanco y amarillo")
    
    @staticmethod
    def cantidadAves():
        return len(Ave.lista)
    
    def movimiento(self):
        return "volar"
    
    def getColorPlumas(self):
        return self.color_plumas