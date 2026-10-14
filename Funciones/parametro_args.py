# Forma no optima de sumar valores
#def suma(a,b):
#    return a+b
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

# Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

# Lo mismo pero utilizando el parametro args
def suma(nombre, *numeros):
  return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"




resultado = suma("Oscar", 5, 6, 7, 8, 9, 12, 3)
resultado = suma_total([1,2,2,4,5,6,7])
print(resultado)