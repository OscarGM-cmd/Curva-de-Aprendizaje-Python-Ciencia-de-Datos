
#Se le pide al usuario entradas separadas por comas, posteriormente que el usuario las introduzca el output es la multiplicacion de las horas por el salario
#antes de eso se convierte dentro del output la hora y el salario a float, dado que estan en cadenas de texto

datos = input('Ingresa primero las horas y posteriormente la paga por hora: ejem: 10,100 \nRespuesta:\t')
hora,salario = datos.split(",")
print(f'La paga debe ser un total de {float(hora) * float(salario)}')