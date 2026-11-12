class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre



oscar = Persona("Oscar",19)

nombre = oscar.nombre
print(nombre)

oscar.nombre = "Juan"
nombre = oscar.nombre
print(nombre)

del oscar.nombre
print(oscar.nombre)