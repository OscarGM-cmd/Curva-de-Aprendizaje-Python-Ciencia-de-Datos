"""
Se crea una lista con la funcion de lista
"""
lista = list(["Hola","Oscar",34])

cadena = "Hola"
"""
Devuelve la cantidad de elementos en una lista
"""
resultado = len(lista)
"""
Se agrega un elemento a la lista pero al ultimo indice
"""
lista.append("1")
"""
Se agrega un elemento a una lista pero en un indice especifico
"""
lista.insert(0,"Primero")
"""
Agrega varios elementos de una lista a otra
"""
lista.extend([False,51])
"""
Elimina elemento de una lista por indice
"""
lista.pop(0)
"""
Remueve un elemento de una lista por su valor, pero si no lo encuentra muestra error
"""
lista.remove("1")
"""
Ellimina todos los elementos de una lista
"""
#lista.clear()
"""
Ordena todos los elementos de manera descendente, unicamente si son valores numericos o booleanos
en caso contrario muestra error, existe el parametro reverse que ordena de mayor a menor
"""
#lista.sort(reverse=True)
"""
Invierte los elementos de una lista
"""
lista.reverse()
"""
Busca en donde se encuentra dicho elemento en una lista
"""
X = lista.index(51)


print(X)