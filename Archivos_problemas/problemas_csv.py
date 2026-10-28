# Cambiar el tipo de dato de columna
import pandas as pd
df = pd.read_csv("Archivos_problemas_resueltos\\datos.csv")
# Convertir a string los datos de una columna
#df['edad'] = df['edad'].astype(str)
# Mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))
# Remplazando los "Galvan" por "Maestro"
df['apellido'].replace("Galvan","Maestro",inplace=True)

# Mostrando la columna apellido
print(df['apellido'])

# Eliminando las filas con valores vacios
df = df.dropna()

# Elliminar las filas repetidas
df = df.drop_duplicates()

# Creando un csv con el dataframe resultante (limpio)
df.to_csv("Archivos_problemas_resueltos\\datosLimpios.csv")