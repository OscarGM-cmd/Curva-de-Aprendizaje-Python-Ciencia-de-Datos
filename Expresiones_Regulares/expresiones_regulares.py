import re 
texto = '''Hola señor, esta es la cadena 1, como estas?,
Esta es la linea 2 de texto
y Esta es la linea 3 de texto'''
# Haciendo una busqueda simple con search
#resultado = re.search("Hola",texto)

# Haciendo una busqueda simple con findall
#resultado = re.findall("Esta",texto,)

#\d -> busca digitos numericos del 0 - 9
#resultado = re.findall(r"\d",texto)

#\D -> busca todo menos digitos numericos del 0 - 9
#resultado = re.findall(r"\D",texto)

#\w -> Busca caracteres alfanumericos desde (A-Z, a-z, 0-9, _)
#resultado = re.findall(r"\w",texto)

#\W -> Busca todo menos los alfanumericos desde (A-Z, a-z, 0-9, _)
#resultado = re.findall(r"\W",texto)

#\s -> Busca espacios en blanco (espacios, tabs, saltos de linea)
#resultado = re.findall(r"\s",texto)

#\S -> Busca todo menos los espacios en blanco (espacios, tabs, saltos de linea)
#resultado = re.findall(r"\S",texto)

#. -> Busca todo menos saltos en linea
#resultado = re.findall(r".",texto)

#\n -> Busca saltos en linea
#resultado = re.findall(r"\n",texto)

#\ -> Cancelacion de caraceteres especiales, cancelando la funcion de punto y buscando puntos
#resultado = re.findall(r"\.",texto)

# Armando una cadena que busque un numero, seguido de un punto y espacio
#resultado = re.findall(r'\d+\.\s', texto)

#^ -> Bsca el comienzo de una linea (Buscando hola al principio de la linea)
# flags=re.M activa la multilinea
resultado = re.findall(f'^Esta',texto,flags=re.M)

print(resultado)