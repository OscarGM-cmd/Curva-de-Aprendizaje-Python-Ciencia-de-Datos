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

def IngresarDatosyOrdenar(texto):
    edades_lista = [item.strip() for item in texto.split(",")]
    nombres = edades_lista[0::2]
    edades = [int(x) for x in edades_lista[1::2]]
    parejas = list(zip(nombres, edades))
    parejas.sort(key=lambda x: x[1])
    Asistente = parejas[0]  
    Docente = parejas[-1]   
    alumnos_ordenados = parejas[1:-1]
    return alumnos_ordenados, Docente, Asistente

entrada = input("Ingresa el nombre y edad (Juan,12,Luis,13,Pedro,45,Ana,10): ")
alumnos, docente, asistente = IngresarDatosyOrdenar(entrada)
alumnos_texto = ", ".join([f"{nom} ({edad} años)" for nom, edad in alumnos])

print(f"\n(A) Los alumnos ordenados de menor a mayor son: {alumnos_texto}")
print(f"(B) El profesor es {docente[0]} con una edad de: {docente[1]} años")
print(f"    El asistente es {asistente[0]} con una edad de: {asistente[1]} años")