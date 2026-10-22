# Un usuario quiere saber todos los numeros primos a partir de cualquier numero que ingrese de forma decreciente, el objetivo
# mostrar unicamente los numeros primos que hay desde ese valor en recesion

def NumerosPrimos(numero):
    Primos = []
    if numero < 2:
        print("No existen numeros primos menores a 2")
        return Primos

    for i in range(2, numero+1):
        primo = True
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                primo = False
                break
        if primo:
            Primos.append(i)
    return Primos
numeros = int(input("Ingresa el numero: "))
x = NumerosPrimos(numeros)
print(f'Tus numeros primos son: {x}')
    