import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leyendo el csv
df = pd.read_csv("Archivos_problemas_graficos\\bigotes.csv")
# Asignacion de valores graficos de x e y, provenientes de df
sns.boxplot(x="categoria",y="valor",data=df)

# Creando un grafico 
plt.show()