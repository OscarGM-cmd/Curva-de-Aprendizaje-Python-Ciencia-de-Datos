class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nom = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'El estudiante {self.nom} está estudiando')

# Interacción con el usuario
nombre = input("Ingresa el nombre: ")
edad = input("Ahora ingrese la edad: ")
grado = input("Ingresa el grado: ")

# Creación del objeto
estudiante = Estudiante(nombre, edad, grado)

print(f"""
DATOS DEL ESTUDIANTE: 

Nombre: {estudiante.nom}
Edad: {estudiante.edad}
Grado: {estudiante.grado}
""")

# Bucle de interacción
while True:
    est = input("Escribe 'estudiar' para que el alumno comience: ")
    
    # .lower() convierte todo a minúsculas, por lo que comparamos con 'estudiar'
    if est.lower() == 'estudiar':
        estudiante.estudiar()  # Llamamos al método desde el objeto creado
        break
    else:
        print("Ingresa la palabra 'estudiar' únicamente.\n")

print("Gracias por usar el programa")
