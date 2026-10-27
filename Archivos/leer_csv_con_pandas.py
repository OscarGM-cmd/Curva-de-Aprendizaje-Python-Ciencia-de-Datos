import pandas as pd
# Usando la funcion read_csv para leer el archivo csv
x = pd.read_csv("Archivos\\datos.csv")
x2 = pd.read_csv("Archivos\\datos.csv")
# Obteniendo los datos de la columna nombre
#nombres = x["name"]

# Ordenando el dataframe por edad
ordenasc = x.sort_values("edad")

# Ordenandolo de forma descendente
ordendesc = x.sort_values("edad",ascending=False)

# Concatenando los dos datas frames
concatenados = pd.concat([x,x2])

# Accediento a la primer fila con head
primerfila = x.head(3)

# Accediento a las terceras ultimas filas
ultiamsfilas = x.tail(3)

# Accediendo la cantidad de filas y columnas con shape
filas_totales,columnas_totales = x.shape

# Obteniendo data estadistica del dataframe
informacion = x.describe()

# Accediendo a un elemento especifico del csv con loc, accediendo al elemento 2 
elemento_especifico_fila = x.loc[2,"edad"]

# Accediendo a un elemento especifico del csv con iloc, accediendo al elemento 2
elemento_especifico_indice = x.iloc[2,2]

# Accediendo a todos los apellidos con iloc
elementos_de_fila = x.iloc[:,1]

# Accediendo a la fila 3 con iloc
elementos_de_fila = x.iloc[2,:]

# Accediendo a las filas con edad mayor que 30
mayor_que = x.loc[x["edad"]>30,:]
print(mayor_que)
