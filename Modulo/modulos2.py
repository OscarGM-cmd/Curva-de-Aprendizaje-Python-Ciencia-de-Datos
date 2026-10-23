# Si el mopdulo estuviera dentro de una carpeta en la misma ruta
# import funciones_buenas.saludar as m_saludar

import sys
sys.path.append("C:\\Users\\ICEL\\Documents\\Python\\Curva-de-Aprendizaje-Python-Ciencia-de-Datos\\Modulo\\FuncionesBuenas")
import saludar as modulo_Saluda
print(f'{modulo_Saluda.saludar("Juan")}')

