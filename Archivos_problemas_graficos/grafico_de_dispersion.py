import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leyendo el csv
df = pd.read_csv("Archivos_problemas_graficos\\dispersion.csv")

# Asignacion de valores graficos de x e y, provenientes de df
sns.scatterplot(x="tiempo",y="dinero",data=df)

# Creando un grafico 
plt.show()