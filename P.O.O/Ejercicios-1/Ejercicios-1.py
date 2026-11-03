class Estudiante:
    def __init__ (self, nombre, edad, grado):
        self.nom = nombre
        self.edad = edad
        self.grado = grado

estudiante1 = Estudiante("Pedro",23,3)

print(estudiante1.nom)