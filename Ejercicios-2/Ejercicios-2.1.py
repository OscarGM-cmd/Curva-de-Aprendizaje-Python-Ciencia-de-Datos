"""
1 Alumno es profesor
1 Alumno es asistente
(A)
Pedir la edad de los compañeros que vinieron hoy a clase y
poner los datos de mayor a menor
(B)
El mayor de la clase es el profesor y
el menor es el asistente
¿Quien es quien?
solucion del curso:
def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingresa el nombre del compañero: ")
        edad = int(input("Ingresa la edad del compañero"))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    docente = compañeros[-1][0]
    return asistente, docente

asistente,profesor = obtener_compañeros(5)

print(f'El profesor es: {profesor} y su asistente es: {asistente}')
"""

def IngresarDatosyOrdenar(datos):
    DatosLista = [item.strip() for item in datos.split(",")]
    Alumnos = DatosLista[0::2]
    Edades = [int(x) for x in DatosLista[1::2]]
    Juntos = list(zip(Alumnos,Edades))
    Juntos.sort(key=lambda x: x[1])
    Asistente = Juntos[0]
    Docente = Juntos[-1] 
    Alumnos = Juntos[1:-1]
    return Alumnos,Asistente,Docente

entrada = input("Ingresa los alumnos (Juan,10,Diego,5,Pedro,21,Young,50): ")
Alumnos,Asistente,Docente = IngresarDatosyOrdenar(entrada)
Alumnos_texto = ", ".join([f"{nom} ({edad} años)" for nom, edad in Alumnos])
print(f"""
(A)
-----------------------------------------------------------------------------------------------------------------------------------
   Los alumnos ordenados de mayor a menor son:
   {Alumnos_texto}
-----------------------------------------------------------------------------------------------------------------------------------

(B)
-----------------------------------------------------------------------------------------------------------------------------------
   El profesor es {Docente[0]} y su edad es {Docente[1]}
   El asistente es {Asistente[0]} y su edad es: {Asistente[1]}
-----------------------------------------------------------------------------------------------------------------------------------
   """)