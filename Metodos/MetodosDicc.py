dicccionario = {
    "Nombre" : "Oscar",
    "Apellido" : "Galvan",
    "Carrera" : "Ingenieria en Sistemas Computacionales",
    "Años" : 20,
    "RFC" : True
}
#Nos devuelve un objeto dict_item
claves = dicccionario.keys()
#Obteniendo un elemento con get, el elemento que se encuentra en Nombre
obtener = dicccionario.get("Nombre")
#Ellimando todo del diccionario
#dicccionario.clear()
#Elliminando elementoS del diccionario
#dicccionario.pop()
#Obteniendo un elemento dict_item iterable
diccionario_iterable = dicccionario.items()
print(diccionario_iterable)