#Entero representado por int, python automaticamente lo dededuce
Ent = 10
#Flotante se trata de un numero con punto decimal
Flot = 10.1
#Número complejo, se tratan de variables con enteros
Comp = 1j + 45
#Cadena de caracteres, se tratan de cualquier letra o caracter dentro de comillas
Cara = 'Sistemas'
#Booleano, se tratan de valores o condiciones, verdadero o falso
Boole = True
#Mapa o diccionario
Dicc = {
    "Carrera": "Sistemas",
}
#Listas se tratan de conjuntos lineales con el objetivo de almacenar datos mutables
Lista = ["Sistemas"]
#Tuplas son conjuntos lineales con la caracteristica de no ser mutables
Tupla = ("Sistemas","Computacionales")
#Conjunto, se trata de estructuras mutables con una coleccion desordenada
Con = {"Sistemas"}
#Conjunto inmutable, coleccion desordenada pero inmutable
ConInm = frozenset(["Sistemas"])
#Rango se trata de una secuencia de cierto punto minimo a maximo donde se puede escoger la posicion
Ran = range(5,10)
#Binario, se trata de el numero de bytes que existe en ese tipo
Bin = bytes(35)

pregunta = input("Comprueba los tipos de datos de python: \n"
"1. Entero\n2. Flotante\n3.Complejos\n4. Caracteres o string\n5. Booleanos\n6. Diccionarios\n7. Listas\n8. Tuplas\n9. Conjuntos\n10. Conjuntos inmutables\n11. Rango\n12. Binarios\nRespuesta: \t")
if pregunta == "1" or pregunta.lower() == "entero":
    print(type(Ent))
elif pregunta == "2" or pregunta.lower() == "flotante":
    print(type(Flot))
elif pregunta == "3" or pregunta.lower() == "complejos":
    print(type(Comp))
elif pregunta == "4" or pregunta.lower() == "caracteres" or pregunta.lower() == "string":
    print(type(Cara))
elif pregunta == "5" or pregunta.lower() == "booleanos":
    print(type(Boole))
elif pregunta == "6" or pregunta.lower() == "diccionarios":
    print(type(Dicc))
elif pregunta == "7" or pregunta.lower() == "listas":
    print(type(Lista))
elif pregunta == "8" or pregunta.lower() == "tuplas":
    print(type(Tupla))
elif pregunta == "9" or pregunta.lower() == "conjuntos":
    print(type(Con))
elif pregunta == "10" or pregunta.lower() == "conjuntos inmutables":
    print(type(ConInm))
elif pregunta == "11" or pregunta.lower() == "rango":
    print(type(Ran))
elif pregunta == "12" or pregunta.lower() == "binarios":
    print(type(Bin))
else:
    print('No se encontro nada')
