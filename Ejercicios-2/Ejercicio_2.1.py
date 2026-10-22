"""
1 Alumno es un profesor
1 Alumno es un asistente
(A)
Pedir la edad de los compañeros que vinieron hoy a clase
y ordenar los datos de menor a mayor
(B)
El mayor es el profesor y el menor es el asistente:
¿Quien es quien?
Solucion del curso:
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

# Solucion propia con respecto a lo aprendido:
def InputYClean(datos):
    DatosLista =  [item.strip() for item in datos.split(",")]
    Nombres = DatosLista[0::2]
    Edades = [int(x) for x in DatosLista[1::2]]
    Grupo = list(zip(Nombres,Edades))
    Grupo.sort(key=lambda x:x[1])
    Docente = Grupo[-1]
    Asistente = Grupo[0]
    Alumnos = Grupo[1:-1]
    return Docente,Asistente,Alumnos

entrada = input("Ingresa el nombre y luego la edad del alumno (Juan,10,Luis,13,Bronco,21): ")
docente,asistente,alumno = InputYClean(entrada)
alumnos_formato = ", " .join([f"{nom} ({edad} años)" for nom,edad in alumno])

print(f"""
(A)
    Los alumnos ordenados de menor a mayor son: 
    {alumnos_formato}
(B)
    El docente es: {docente[0]} y tiene {docente[1]} años
    El asistente es: {asistente[0]} y tiene {asistente[1]} años
""")