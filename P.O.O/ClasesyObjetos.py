# Se solicita crear un programa para crear celulares

# Esta es la forma menos optima de celulares
# celular1_marca = "Samsumg"
# celular2_marca = "Apple"
# celular3_marca = "Huawei"

# celular1_modelo = "S23"
# celular2_modelo = "Iphone 15 pro"
# celular3_modelo = "P20 pro"

# celular1_camaraT = "48MP"
# celular2_camaraT = "48MP"
# celular3_camaraT = "12MP"

# celular1_camaraF = "24MP"
# celular2_camaraF = "24MP"
# celular3_camaraF = "48MP"


# Clase fija
# class Celular():
#     marca = "Samsumg"
#     modelo = "S23"
#     camara = "48MP"

# celular1 = Celular()
# print(celular1.camara)


# Primera clase con datos no fijos
class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara


celular1 = Celular("Samsumg","S23","48MP")
celular2 = Celular("Apple","Iphone 15 pro","48MP")

print(celular1.marca)
