"""
Existen dos listas una con nombres y la otra con apellidos, escribir los datos en un archivo de texto de forma optima
con un bucle for
"""
listaNombre = ["Juan","Luis","Oscar"]
lsitaApellido = ["Galvan", "Martinez","Reza"]

with open("Archivos_problemas_resueltos\\problema_txt.txt",'a',encoding="UTF-8") as pbtxt:
    for i in listaNombre:
        pbtxt.write(f'{listaNombre[i]} {lsitaApellido[i]}\n')
