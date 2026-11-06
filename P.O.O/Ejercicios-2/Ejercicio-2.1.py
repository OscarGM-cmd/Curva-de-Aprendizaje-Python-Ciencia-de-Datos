# Herencias - Ejercicio 2
# Ejercicio de herencia y uso de super:
# Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales:
#  Persona y Estudiante. La clase Persona tendra los atributos de nombre y edad y un metodo que imprima
#  el nombre y la edad de la persona. La clase Estudiante heredará de la clase Persona y tambien tendra un atributo adicional
#  el atributo adicional es grado y un metodo que imprima el grado del Estudiante
#  Deberas utilizar super en el metodo de inicializacion (init) para reutilizar el codigo de la clase padre.
#  luego crea una instancia de la clase estudiante e imprime sus atributos y utiliza sus metodos para asegurarte que todo funciona

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre 
        self.edad = edad
    def Mostrar_Datos(self):
        return(f'{self.nombre}, {self.edad} años')

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    
    def Mostrar_Grado(self):
        return(f'grado: {self.grado}')

Pedro = Estudiante("Pedro",18,3)

print(f'Hola soy {Pedro.Mostrar_Datos()} y estoy en {Pedro.Mostrar_Grado()}')