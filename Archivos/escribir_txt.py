with open("Archivos\\texto.txt",'a' ,encoding="UTF-8") as archivo:
    # Se remplaza todo el bloc de notas por lo que este escrito:
    # archivo.write("Se ingresan datos a txt...")
    archivo.write("\n")
    # Agregando 2 lineas con writelines
    #archivo.writelines(["Hola\n","que ","tal ","como ","estas"])
    # Agregando 2 lineas extra con writelines
    #archivo.writelines(["\nBien,\n","que ","tal ","como ","estas tu"])
    for i in range(5):
        archivo.write(f'La linea {i+1} agregadada\n')
    
    