# Abriendo el archivo con with open
with open("Archivos\\texto.txt",encoding="UTF-8") as Archivo:
    # Leyendo el archivo
    contenido = Archivo.read
    # Mostrando el archivo
    print(contenido)
# No es necesario cerrarlo porque estamos usando with open