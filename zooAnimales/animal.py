from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil

class Animal:
    totalAnimales=0

    def __init__(self,nombre: str=None,edad: int=None,habitat:str=None,genero: str=None):
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.zona=None
        Animal.totalAnimales+=1

    def movimiento(self) -> str:
        return "desplazarse"
    
    @staticmethod
    def totalPorTipo() -> str:
        return(f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}Peces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}")
    
    def toString(self) -> str:
        if self.zona==None:
            return(f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}")
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}, la zona en la que me ubico es {self.zona.get_nombre()}, en el {self.zona.get_zoo().get_nombre()}."
        
    def getNombre(self) -> str:
        return self.nombre
    
    def getEdad(self) -> int:
        return self.edad
    
    def getHabitat(self) -> str:
        return self.habitat
    
    def getGenero(self) -> str:
        return self.genero
    