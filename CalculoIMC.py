"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""
# Este bloque de codigo funciona gracias a que se declara una variable flotante, usando funciones como float() y input(), se aplica la misma logica para estatura,
# posteriormente se declara una variable denominada imc y esta funciona como ejecucion del calculo aritmetico, peso / estatura ^ 2
peso = float(input("Ingresa el peso (en kg): "))
estatura = float(input("Ingresa la estatura (en metros): "))
imc = peso/pow(estatura,2)
print(imc)

