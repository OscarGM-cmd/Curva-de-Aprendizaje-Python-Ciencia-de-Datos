class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'Impresionante, cometiste el siguiente error: {err}')


# Lanzando una excepcion propia
# raise MiExcepcion("Fallo realmente")

# Manejando una exepcion propia
try:
    raise MiExcepcion("Jajaja, fallase")
except:
    print("Como cometiste ese error?")


