"""
Existen dos listas una con nombres y la otra con apellidos, escribir los datos en un archivo de texto de forma optima
con un bucle for
solucion del curso:
nombres = ["Lucas", "Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Dalto","Robertikx","Carado"]

with open("archivos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son: \n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------\n") for n,a in zip(nombres,apellidos)]
"""
nombres = input("Ingresa los nombres separados por comas: (Juan, Luis, Enrique, Oscar, etc.): ")
apellidos = input("Ingresa los apellidos separados por comas: (Galvan, Moncada, Martinez, Mendoza, etc.): ")
listaNombre = [x.strip() for x in nombres.split(",")] 
listaApellido = [x.strip() for x in apellidos.split(",")] 

with open("Archivos_problemas_resueltos\\problema_txt.txt",'a',encoding="UTF-8") as pbtxt:
    [pbtxt.write(f'{listaNombre[i]} {listaApellido[i]}\n') for i in range(len(listaNombre))]