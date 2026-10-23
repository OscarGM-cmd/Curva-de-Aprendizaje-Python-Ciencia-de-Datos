# Importando un modulo y asignandole el nombre "saludo"
#import modulo_saludar as saludo

# Desde este modulo, importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar as Saludo,saludarRaro as SaludoRaro
import modulo_saludar as m_saludar
# Creamos dos variables a las cuales les asignamos el valor de las funciones con "Juan"
saludo = Saludo("Juan")
saludoraro = SaludoRaro("Juan")

# Mostramos los resultados
print(saludo)
print(saludoraro)

# Para ver las propiedades y metodos del namespace
#print(dir(__name__))
# Accedemos al nombre del modulo que usemos
#print(m_saludar.__name__)
# Importamos el modulo subsaludar desde una carpeta que no se encuentra en el mismo directorio
from SubCarpeta.modulo_subsaludar import saludar2 as sld2,saludare as sldr