# Creacion de diccionario por medio de funcionj con dict()
diccionario = dict(nombre='Oscar',Apellido='Galvan')

# Las listan no pueden ser claves y se usa frozzen set para conjuntos
diccionario = {frozenset(["dato 1", "dato 2"]): "jua" , ("Dato 1","Dato 2"): "jeje"}

# Creacion de diccionarios con fromkeys con valor none
diccionario = dict.fromkeys(["nombre","apellido"])

# Creacion de diccionarios con fromkeys con valor a "Desconocido"
diccionario = dict.fromkeys(["nombre","apellido"], "Desconocido")

print(diccionario)

