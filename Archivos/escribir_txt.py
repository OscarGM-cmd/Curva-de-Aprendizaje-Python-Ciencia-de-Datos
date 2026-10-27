with open("Archivos\\texto.txt",'w' ,encoding="UTF-8") as archivo:
    # Se remplaza todo el bloc de notas por lo que este escrito:
    # archivo.write("Se ingresan datos a txt...")
    archivo.writelines(["Hola\n","que ","tal ","como ","estas"])
    archivo.writelines(["\nBien,\n","que ","tal ","como ","estas tu"])
    