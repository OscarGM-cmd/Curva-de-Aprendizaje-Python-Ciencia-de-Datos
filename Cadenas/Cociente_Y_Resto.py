"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""
# Se declaran dos variables input denominadas n y m, estas se convierten en int o enteros, para ser usadas posteriormente
# en un output se muestra el resultado y se calcula dentro de estas usando operadores como // y % que es para obtener el entero sin residuo y el modulo
n = int(input("Ingresa un numero numerador: "))
m = int(input("Ingresa un denominador: "))
print(f'El resultado de: {n} / {m} nos da que el cociente es igual a: {n // m} y un resto de {n % m}')
