import re
# Cadena de texto de ejemplo para un correo electronico
email = "example@example.com"

# El patron nos dice que va a tomar desde la a hasta la z minusculas (a-z), despues nos dice que tomara desde la A hasta la Z en mayusculas (A-Z), posteriormente dice que tomara en cuenta desde el 0 hasta el nueve (0-9),
# despues dice que tomara en cuenta unicamente guion bajo, simbolo de porcentaje, simbbolo de mas y simoblo de menos (.-%+-) y luego nos dice que almenos debe haber uno o mas ([]+)
# despues dice que tiene que tener un @ y este debe ser seguido por algun caracter desde la a hasta la z en minusculas o A hasta la Z en mayusculas
# posteriormente toma en cuenta si existe algun numero del 0 al 9 en ese modulo, dice que permite unicamente el caracter guion (-), todo ese modulo tiene que tener almenos uno
# posteriormente tiene que estar seguido de un ., con un modulo que tenga desde la a a la z en minusculas o a a la z en mayusculas, minimo 2 caracteres hasta los que sean
patron = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# El resultado sera igual a la comparacion de el patron con la cadena de texto
resultado = re.match(patron,email)

# Verificacion de si el correo es valida
if resultado:
    print("Direccion de correo valida")
else:
    print("Direccion de correo invalida")