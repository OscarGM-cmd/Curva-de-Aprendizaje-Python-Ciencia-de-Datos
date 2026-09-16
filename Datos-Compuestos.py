"""
Las listas son mutables y estas pueden cambiarse con el indice, son mutables
"""
lista = ["Oscar Galvan", "Soy Oscar", True, 1.70]
"""
Las tuplas no se pueden modificar, no son mutables
"""
tupla = ("Oscar Galvan", "Soy Oscar", True, 1.70)
#print(tupla[0])

"""
Creacion de conjunto (Set) no tienen orden fijo pero no muestra valores repetidos
"""
conjunto = {"Oscar Galvan", "Soy Oscar", True, 1.70}

"""
Diccionario, son similares a una lista pero tu decides como llamar al indice, mediante claves y valores
"""
diccionario = {
    'Nombre' : "Oscar Galvan",
    'Saludo' : "Soy Oscar",
    'Valor' : True,
    'Altura' : 1.70,
    'Duplicado' : "Soy oscar"
}

print(diccionario["Altura"] + 2)