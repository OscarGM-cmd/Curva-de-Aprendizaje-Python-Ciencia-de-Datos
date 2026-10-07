"""
Ejercicio 1.1:
Existe un curso que enseña en 1.5 horas a programar en Python, este tiene la ventaja que enseña
la misma cantidad de contenido que otro curso con un minimo de 2.5 horas, a su ves el promedio de cursos
para llegar a esa cantidad de contenido es de 4 horas, mientras que el maximo de tiempo visto para llegar a
ese contenido es de 7 horas, sin embargo esos cursos en crudo, cuando no estan editados todavia,
duran minimo 2.5 el curso principal, 3.5 horas el curso minimo y 5 horas el curso promedio.
lo que se pide es:
a) Diferencia en porcentaje entre el curso principal y:
- El mas rapido de otros cursos
- El mas lento de otros cursos
- El promedio de otros cursos
b) Porcentaje de material inservible que se reduce en:
- El promedio de los cursos
- El curso actual
c) Ver 10 horas de ese curso a cuantas horas equivale en otros cursos, y cuanto tiempo es en el caso contrario
"""
lisPrin = [1.5]
lisOtros = [2.5, 4, 7]
lisOtrosCrudo = [3.5, 5]
lisPrinCrudo = [2.5]
lisOtros.sort()

print(f"""
a)
- La diferencia porcentual entre mas rapido de otros cursos comparado con el principal es: {(((lisOtros[0]-lisPrin[0])/lisOtros[0]) * 100):.2f}%
- La diferencia porcentual entre mas lento de otros cursos comparado con el principal es: {(((lisOtros[-1]-lisPrin[0])/lisOtros[-1]) * 100):.2f}%
- La diferencia porcentual entre el promedio de otros cursos comparado con el principal es: {(((lisOtros[(int(len(lisOtros))) // 2]-lisPrin[0])/lisOtros[(int(len(lisOtros))) // 2]) * 100):.2f}%
b)
- El porcentaje de material inservible que se reduce en el promedio de otros cursos es de: {(((lisOtrosCrudo[-1]-lisOtros[(int(len(lisOtros))) // 2])/lisOtrosCrudo[-1]) * 100):.2f}
- El porcentaje de material inserbible que se reduce en el promedio de este curso es de: {(((lisPrinCrudo[0]-lisPrin[0] )/ lisPrinCrudo[0])*100):.2f}
c) 
- Ver 10 horas en el curso principal equivale a {((10 * lisOtros[0])/lisPrin[0]):.2f} horas en el curso con duracion minima
- Ver 10 horas en el curso principal equivale a {((10 * lisOtros[-1])/lisPrin[0]):.2f} horas en el curso con duracion maxima
- Ver 10 horas en el curso principal equivale a {((10 * lisOtros[(int(len(lisOtros))) // 2])/lisPrin[0]):.2f} horas en el curso con duracion promedio
- Ver 10 horas en el curso de duracion minima de otros equivale a {((10*lisPrin[0])/lisOtros[0]):.2f} del curso principal
- Ver 10 horas en el curso de duracion maxima de otros equivale a {((10*lisPrin[0])/lisOtros[-1]):.2f} del curso principal
- Ver 10 horas en el curso de duracion promedia de otros equivale a {((10*lisPrin[0])/lisOtros[(int(len(lisOtros))) // 2]):.2f} del curso principal
""")


