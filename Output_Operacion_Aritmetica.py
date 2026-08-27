lista = []
for i in range(0, 4):
    print(f'Ingresa el valor de el modulo {i}: ')
    x = input()
    lista.append(x)

res = pow(((float(lista[0]) + float(lista[1]))) / (float(lista[2]) * (float(lista[3]))), 2)
print(f'El resultado es: {res}')