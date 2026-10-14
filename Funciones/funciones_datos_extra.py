
# Creando una funcion de 3 parametros
def frase1(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

# Utilizando keyword arguments
frase_resultante = frase1(adjetivo="Capo",apellido="Lopez",nombre="Juan")


# Creando la misma funcion usando un atributo como valor por defecto
def frase2(nombre,apellido,adjetivo = "Bodrio"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante = frase(adjetivo="capo",nombre="Juan",apellido="Lopez")
print(frase_resultante)