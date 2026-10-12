# Asignacion de valor, de variables
animales = ["gato","perro","loro","cocodrilo"]
numeros = (10,213,213,132)
# Bucle for que meustra todos los elementos de una lista
for animal in animales:
    print(f'Ahora tu animal es igual en: {animal}')

# Bucle for que muestra todos los elementos de una lista multiplicados por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
# Bucle, for para iterar dos conjuntos del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f'Recorriendo lista 1: {numeros}\nRecorriendo Lista 2: {animales}')
    
# Forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])

# Forma optima de recorrer una lista
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')

# Usando el else junto con for
for num in numeros:
    print(f'Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("El bucle termino")