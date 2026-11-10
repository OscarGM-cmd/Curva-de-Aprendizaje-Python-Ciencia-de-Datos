# Ejercicio de herencia multiple y MRO:
# Imagina que estas modelando animales en un zoologico. CREAR TRES CLASES: "Animal", "Mamimefero" y
# "Ave". La clase "Animal" debe tener un metodo llamado "comer". La clase "Mamifero" debe tener un metodo llamado
# "amamantar" y la clase "Ave" debe tener un metodo llamado "volar".

# Ahora crea una clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden y por lo tanto debe ser capaz
# de "amamantar" y "volar", ademas de "comer"

# Finalmente, juega con el orden de la herencia de la clase "Murcielago" y observa como cambia el MRO y 
# el comportamiento de los metodos al usar super().

class Animal:
    def __init__(self):
        pass
    def comer(self):
        return(f'comiendo...')
    
    
# Realmente tiene la herencia del animal pero se desvinculo para poder comprobar el MRO
class Mamifero(Animal):
    def amamantar(self):
        return(f'amamantando...')
    def comer(self):
        return(f'comer')
    def volar(self):
        return(f'vole')

    
# Se desvinculo el animal para poder tener uso de MRO
class Ave(Animal):
    def __init__(self):
        pass
    def volar(self):
        return(f'volando....')
    def comer(self):
        return(f'comer')
    def amamantar(self):
        return(f'amamantado')
    
# Murcielago hereda de ave y mamifero, cuyas clases a su vez heredan de animal
class Murcielago(Ave,Mamifero):
    def __init__(self):
        Animal.__init__(self)
        Mamifero.__init__(self)
        Ave.__init__(self)

    def MostrarSuper(self):
        comer = super().comer()
        volar = super().volar()
        amamantar = super().amamantar()
        print(f'{comer}\n{amamantar}\n{volar}\n')
    
# Creando una instancia
Murcielagos = Murcielago()
#Mostrando los resultados
print("\nResultados de las funciones de momento\n")
Murcielagos.comer()
Murcielagos.volar()
Murcielagos.amamantar()
print("\nUso de prioridad desde la clases donde la funcion es la valida (clase.funcion(Instancia)\n")
Animal.comer(Murcielagos)
Ave.volar(Murcielagos)
Mamifero.amamantar(Murcielagos)
print("\nUsando super en vez de (clase.funcion(Instancia))\n")
Murcielagos.MostrarSuper()
print("\nPruebas para ver la ramificacion con la funcion mro\n")
print(Murcielago.mro())