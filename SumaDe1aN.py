"""
Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
"""
limite = int(input("Ingresa un numero entero: "))
suma = limite*(limite+1)/2
print(f'Tu resultado de la suma de 1 a {limite} es: {suma}')

