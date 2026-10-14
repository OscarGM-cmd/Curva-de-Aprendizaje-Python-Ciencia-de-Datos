# Creando una funcion simple
# def saludar():
#    print("Hola oscar, ¿Como estas?")
# Ejecutando una funcion simple
# saludar()

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "capo"
    else:
        adjetivo = "amor"
    print(f'Hola {nombre}, mi {adjetivo} ¿Como estas?')
    
saludar("Anahi", "Mujer")
saludar("Oscar","Hombre")
saludar("Alex","No binario")

# Crear una funcion que nos retorne valores
def calculo(num):
    chars = "abcdefghij"
    num_entero = str(num)  
    num = int(num_entero[0])
    c1 = num -2
    c2 = num 
    c3 = num - 5 
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return(contraseña,num)

# Desempaquetando la funcion
resultado1,resultado2 = calculo(392)

# Igualandola en una variable
frase = "Tu contraseña nueva es: " + str(resultado1) + "y tu numero es: " + str(resultado2)

# Mostrando el resultado de la variable
print(frase)