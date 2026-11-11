# Se declara una clase gato con una funcion llamada sonido que regresa un string 
class Gato():
    def sonido(self):
        return "Miau"

# Se declara una clase perro con una funcion llamada sonido que regresa un string
class Perro():
    def sonido(self):
        return "Guau"

# Se declara una funcion que toma como valor de entrada un animal y imprime la funcion sonido de ese animal
def hacer_sonido(animal):
    print(animal.sonido())

# Se crean instancias 
gato = Gato()
perro = Perro()

# Se usa la funcion pasando como valor la instancia
hacer_sonido(gato)

# Se imprime como "regularmente" esta hecha la clase
print(gato.sonido())