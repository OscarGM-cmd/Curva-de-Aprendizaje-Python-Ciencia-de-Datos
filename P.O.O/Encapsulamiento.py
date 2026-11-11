class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

oscar = Persona("Oscar",18)
nombre = oscar.get_nombre()
print(nombre)
oscar.set_nombre("Juan")
nombre = oscar.get_nombre()
print(nombre)