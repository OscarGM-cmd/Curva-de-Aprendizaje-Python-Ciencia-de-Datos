# Creacion de un conjunto con set
conjunto = set(["Dato 1", "Dato 2"])

# Integrando un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato1","Dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

# Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {3,5,7}

# Verificacion de si es un subconjunto
resultado = conjunto1.issubset(conjunto2)
resultado = conjunto2 <= conjunto1
print(resultado)
# Verificacion si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto2 > conjunto1


print(resultado)