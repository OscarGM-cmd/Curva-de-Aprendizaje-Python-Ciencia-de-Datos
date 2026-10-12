diccionario = {
    "nombre" : "Oscar",
    "apellido": "Galvan",
    "numero" : 5533231680
}

# Recorriendo diccionario para obtener las claves
for key in diccionario:
    key
    print(f'La clave es: {key}')

# Recorriendo diccionario con items() para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es {key} y el valor es: {value}')