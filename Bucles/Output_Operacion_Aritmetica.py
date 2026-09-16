#En este bloque de codigo lo que hace es crear una lista con n espacios, luego un ciclo for de 0 a 4 basicamente 4 ciclos, posteriormente
#se le agrego un mensaje en pantalla para depues guardar el valor en x, con append se le guarda el valor al ultimo indice de la lista 
#como esta vacia el ultimo indice de esa lista es -1, despues es 0,1,2,3, la funcion aritmetica era:
#(a+b/c*d)^2
lista = []
for i in range(0, 4):
    print(f'Ingresa el valor de el modulo {i}: ')
    x = input()
    lista.append(x)

res = pow(((float(lista[0]) + float(lista[1]))) / (float(lista[2]) * (float(lista[3]))), 2)
print(f'El resultado es: {res}')