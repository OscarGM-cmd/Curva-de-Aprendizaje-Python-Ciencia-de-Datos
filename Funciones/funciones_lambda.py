numeros = [1,2,3,4,5,6,7]
# Creando una funcion lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x*2

# Creando una funcion que diga si es par o no
def es_par (num):
    if (num%2==0):
        return True
# Usando filter una funcion comun
numeros_pares = filter(es_par,numeros)

# Creando lo visto anterior pero con lambda
numeros_pares2 = filter(lambda numero:numero%2 == 0, numeros)

print(list(numeros_pares2))
