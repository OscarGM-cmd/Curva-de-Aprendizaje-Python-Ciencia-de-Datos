"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
usuario = input("Ingresa un nombre: ")
numero = int(input("Ingresa el numero de veces que quieres que se repita: "))
print(f'{(usuario+ "\n")* 3}')