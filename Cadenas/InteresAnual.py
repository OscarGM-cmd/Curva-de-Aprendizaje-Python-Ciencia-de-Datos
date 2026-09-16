"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""
# En este bloque de codigo se declara tanto una variable flotante como una variable años e interes, estas son input,
# posteriormente se calcula el capital en una variable con la misma denominacion usando su formula 
# se muestra como ultimo en un output el resultado de la inversion
monto = float(input("Ingresa la cantidad a invertir (Enteros): "))
anios = float(input("Ingresa la cantidad de años (Años y): "))
interes = float(input("Ingresa el interes anual (Porcentaje %): "))
capital = monto*(1 + interes/100)** anios
print(f'El capital obtenido en la inversión es: {capital:.2f}')