"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa 
que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
ahorros = float(input("Ingresa cantidad de ahorro: "))
print(f'Inicialmente tus ahorros son: {ahorros} pero en tu ')
ahorros = ahorros + ahorros*4/100 
print(f'Primer año son: {ahorros:.2f}')
ahorros = ahorros + ahorros*4/100 
print(f'Segundo año son: {ahorros:.2f}')
ahorros = ahorros + ahorros*4/100 
print(f'Tercer año son: {ahorros:.2f}')
