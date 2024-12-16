def totalPortTipo() -> str:
    from zooAnimales.ave import Ave
    from zooAnimales.mamifero import Mamifero
    from zooAnimales.reptil import Reptil
    from zooAnimales.pez import Pez
    from zooAnimales.anfibio import Anfibio

    totalReptiles=Reptil.cantidadReptiles()
    totalAves=Ave.cantidadAves()
    totalMamiferos=Mamifero.cantidadMamiferos()
    totalPeces=Pez.cantidadPeces()
    totalAnfibios=Anfibio.cantidadAnfibios()
    salida = f"Mamiferos : {totalMamiferos}\nAves : {totalAves}\nReptiles : {totalReptiles}\nPeces : {totalPeces}\nAnfibios : {totalAnfibios}"
    return salida

if __name__ == "__main__":
    print(totalPortTipo())