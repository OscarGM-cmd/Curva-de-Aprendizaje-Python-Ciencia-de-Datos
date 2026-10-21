# Crear una funcion que al pasar un numero genere numeros primos hasta pasar ese numero

def NumPrimos(numero):
  primos = []
  if numero < 2:
    print("Error, no hay números primos menores a 2")
    return primos

  for i in range(2, numero + 1):
    es_primo = True
    for j in range(2, int(i**0.5) + 1):
      if i % j == 0:
        es_primo = False
        break
    if es_primo:
      primos.append(i)

  return primos


valor = int(input("Ingresa un número: "))
primos = NumPrimos(valor)
print(f"Tus números primos son: {primos}")
