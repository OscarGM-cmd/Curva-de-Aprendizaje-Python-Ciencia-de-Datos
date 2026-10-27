# Usando open para abrir un archvio con codificacion unviersal (UtF-8)
archivo_sin_leer = open("Archivos\\texto.txt",encoding="UTF-8")
# Leer archivo completo
#archivo = archivo.read()
# Leer linea por linea
#linea = archivo_sin_leer.readlines()

# Leer una sola linea
#linea = archivo_sin_leer.readline()

# Cerrar archivo
archivo_sin_leer.close()

print(linea)
