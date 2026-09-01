"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa 
que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
# En este bloque de codigo si bien se puede usar un ciclo for para mostrar el proceso, se usaron cadenas para comprender el funcionamiento de estas en python,
# se declara una variable input de tipo flotante, posteriormente se imprime antes de que cambie esa variable y pueda ser mostrada en pantalla antes de cambios,
# se muta la variable, posteriormente se muestra ese cambio y pasa secuencialmente lo mismo despues hasta el tercer año
ahorros = float(input("Ingresa cantidad de ahorro: "))
print(f'Inicialmente tus ahorros son: {ahorros} pero en tu ')
ahorros = ahorros + ahorros*4/100 
print(f'Primer año son: {ahorros:.2f}')
ahorros = ahorros + ahorros*4/100 
print(f'Segundo año son: {ahorros:.2f}')
ahorros = ahorros + ahorros*4/100 
print(f'Tercer año son: {ahorros:.2f}')
