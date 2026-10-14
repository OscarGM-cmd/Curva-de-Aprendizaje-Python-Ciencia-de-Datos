# Asignacion de valores a una lista
lista = [1, 2, 3, 4, 5]

# Encontrando el numero mayor de una lista
numero_mas_alto = max(lista)

# Encontrando el numero menor de una lista
numero_mas_bajo = min(lista)

# Redondeando numero con round
numero_redondeado = round(12.5678123,2)

# Retorna false si es 0, vacio, false o none y da true si es distinto a 0, si es true, si es una cadena, si es un dato no vacio
resultado_bool = bool(0)

# Retorna true si todos los datos son verdaderos
resultado_all = all([0,"True",[344,233]])

# Suma total de todos los numeros
suma_total = sum(lista)

#Mostrando numero mas pequeño y mas grande de la lista 
print(f'''El numero mas alto es: {numero_mas_alto} y el numero mas bajo es: {numero_mas_bajo}\nEL numero redondeado es: {numero_redondeado}
El resultado de usar la funcion bool es: {resultado_bool}
El resultado de usar la funcion All es: {resultado_all}
El resultado de usar la funcion de sum es: {suma_total}
''')
