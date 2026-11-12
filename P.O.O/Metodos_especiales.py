class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'

oscar = Persona("Oscar",20)

print(oscar)

repre = repr(oscar)
resultado = eval(repre)
print(resultado.edad)