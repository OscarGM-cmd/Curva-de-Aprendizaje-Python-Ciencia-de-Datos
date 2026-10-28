# Creando una funcion que suma dos numeros
def suma():
    # Creamos un bucle for para iterar de nuevo en caso de exepcion
    while True:
        # Variables input para sumar posteriormente
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        # Usamos try en caso de una exepcion
        try:
            resultado = int(a)+int(b)
        # Si resulta la exepcion mostramos en pantalla "Porfavor, ingresa un numero"
        except Exception as e:
            print("Porfavor, ingresa un numero")
            print(f"ERROR: {e}")
        # Si todo sale bien terminamos el bucle
        else:
            break
        # Se ejecuta siempre, sin importar lo que pase
        finally:
            print("Gracias, por intentar")
    # Devolvemos el resultado
    return resultado
print(suma())