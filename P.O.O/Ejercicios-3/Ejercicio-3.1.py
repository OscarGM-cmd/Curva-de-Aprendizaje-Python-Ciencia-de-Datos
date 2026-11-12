import math as m
# Crear un juego de fusión
# El juego consiste en crear personajes de un juego y que esos personajes se puedan fusionar
# para formar personajes mas podersos que tengan mas poder...
# Para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes se
# fusionen, salga un nuevo personaje con habilidades mejoradas.
# una posible formula es: el promedio de las habilidades de ambos al cuadrado

class Personaje():
    def __init__(self,personaje,poder):
        self.personaje = personaje
        self.poder = poder

    def __add__(self,otro):
        nuevo_valor = pow((self.poder + otro.poder)/2,2)
        Iniciales = self.personaje[:3]
        Finales = otro.personaje[3:7]
        return Personaje((Iniciales+Finales),nuevo_valor)

Goku = Personaje("Goku",10000)
Vegetta = Personaje("Vegeta",2000)
Fusion = Goku+Vegetta
print(f'Hola soy {Fusion.personaje} y mi poder es: {Fusion.poder}')
