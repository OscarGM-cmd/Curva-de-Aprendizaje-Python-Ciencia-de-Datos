#Se prueba un condicional para entender la estructura y reglas de este condicional
edad = int(input("Ingresa tu edad: "))

if edad >= 18: 
    print("Puedes pasar")
else:
    print("No puedes pasar")
print("Muchas Gracias por intentar")

contraseña_almacenada = "123"
contraseña_escrita = "123"
if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SESION....")
else:
    print("NEGANDO ACCESO...")