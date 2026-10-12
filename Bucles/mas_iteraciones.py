frutas= ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena_texto = "Hola oscar"

# Evitando que se coma una manzana con la sentencia contunua
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una {fruta}')

# Evitando que se siga ejecuando cuando se va a comer una pera
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voy a comer una {fruta}')
print("Bucle terminado")

# Evitar que se siga ejecutando el bucle (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break
else:
    print("Terminado")

# Recorrer una cadena de texto
for letra in cadena_texto:
    print(letra)