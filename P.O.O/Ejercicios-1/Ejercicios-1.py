# El ejercicio nos dice que hay una clase que se llama estudiante con los atributos: Nombre, Edad y Grado
# nos pide crear un metodo estudiar que tenga un texto "el estudiante (nombre) esta estudiando" crear un objeto estudiante y
# usar el metodo estudiar el usuario puede interactuar 
class Estudiante:
    def __init__ (self, nombre, edad, grado):
        self.nom = nombre
        self.edad = edad
        self.grado = grado

estudiante1 = Estudiante("Pedro",23,3)

print(estudiante1.nom)