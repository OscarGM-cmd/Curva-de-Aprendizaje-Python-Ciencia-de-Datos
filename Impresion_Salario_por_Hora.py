datos = input('Ingresa primero las horas y posteriormente la paga por hora: ejem: 10,100 \nRespuesta:\t')
hora,salario = datos.split(",")
print(f'La paga debe ser un total de {float(hora) * float(salario)}')