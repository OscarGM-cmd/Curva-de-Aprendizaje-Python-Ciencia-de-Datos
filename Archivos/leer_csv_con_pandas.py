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
print(primerfila)
