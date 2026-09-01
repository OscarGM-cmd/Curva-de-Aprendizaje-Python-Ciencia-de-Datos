"""
Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
"""

# Este bloque funciona dado que se convierte en entero el limite, antes de convertirlo a entero se le pide un str con input, posteriormente
# una variable llamada suma hace el calculo aritmetico para el resultado por ultimo usamos la funcion print para imprimir el resultado

limite = int(input("Ingresa un numero entero: "))
suma = limite*(limite+1)/2
print(f'Tu resultado de la suma de 1 a {limite} es: {suma}')