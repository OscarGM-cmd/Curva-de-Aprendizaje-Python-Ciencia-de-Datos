class Persona():
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola, estoy hablando un poco")


class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        super().__init__(nombre,edad,nacionalidad)
        self.notas = notas
        self.universidad = universidad

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return (f'mi habilidad es: {self.habilidad}')

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa 
    def presentarse(self):
        return (f'Hola soy {self.nombre}, tengo {self.edad} años, soy de {self.nacionalidad} y {super().mostrar_habilidad()}, trabajo en {self.empresa} con un salario de {self.salario}')   
juan = EmpleadoArtista("Juan",32,"Mexicano","Cantar",10000,"Coca Cola")

print(juan.presentarse())

es_subclase = issubclass(EmpleadoArtista,Artista)
print(es_subclase)
es_instancia = isinstance(juan,EmpleadoArtista)
print(es_instancia)