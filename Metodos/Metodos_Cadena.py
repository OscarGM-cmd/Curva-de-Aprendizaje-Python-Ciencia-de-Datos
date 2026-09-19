cadena1 = "Hola soy Oscar"
cadena3 = "353531"
cadena4 = "EstoSiEsAlfaNumerico"
cadena2 = "Bienvenido"
"""
La funcion dir nos permite visualizar todos los metodos y posibilidades
que tenemos para dicha variable
"""
cadenadir = dir(cadena1)
"""
Lo que hace el metodo upper es convertir todo a mayusculas
"""
cadenaupper = cadena1.upper()
"""
Lo que hace el metodo lower es convertir todo a minisculas
"""
cadenalower = cadena1.lower()
"""
Lo que hace el metodo capitalize es convertir la primer letra en mayusculas 
pero antes hace todas las letras en minusculas, despues la primer letra en mayusculas
"""
cadenacapitalize = cadena1.capitalize()
"""
Buscamos una cadena en otra cadena peros i no hay coincidencia devuelve -1
"""
cadenafind = cadena1.find("")
"""
Buscamos una cadena dentro otra cadena pero si no encuentra nada da error
"""
cadenaindex = cadena1.index("")
"""
Si el valor es numerico devuelve true, si no es numerico devuelve false
"""
cadenaisnumeric = cadena3.isnumeric()
"""
Si el valor es alfa numerico devuelve true, si no es alfanumerico devuelve false
"""
cadenaisalpha = cadena4.isalpha()
"""
Count lo que hace es contar las veces que encuentra una coincidencia con respecto de una cadena en otra cadena
"""
cadenacount = cadena1.count("a")
"""
Len cuenta cuantos caracteres tiene una cadena
"""
cadenalen = len(cadena1)
"""
Verifica si una cadena empieza con otra cadena dada, si es asi devuelve True
"""
cadenastartswith = cadena1.startswith("H")
"""
Verifica si una cadena termina con otra cadena dada, si es asi devuelve True
"""
cadenaendswith = cadena1.endswith("ar")
"""
Remplaza un pedazo de la cadena dada por una cadena 
"""
cadenareplace = cadena1.replace("Hola", "Bienvenido")
"""
Split lo que hace es crear una lista pero separandola por una cadena
"""
cadenasplit = cadena1.split(" ")


print(cadenasplit[0])
