import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Archivos_problemas_graficos\\fallos.csv")
sns.lineplot(x="fecha",y="errores",data=df)
plt.plot("01-09",17,"o")
plt.show()