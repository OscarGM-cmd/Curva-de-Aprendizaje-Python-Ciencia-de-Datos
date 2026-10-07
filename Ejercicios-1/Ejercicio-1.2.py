"""
Los parametros son que en 1 segundo dice 2 palabras cuantos segundos x palabras
a) Pedirle al usuario que diga cualquier texto real y:
- Calcular cuanto tardara en decir esa frase
- ¿Cuantas Palabras dijo?
b) Si tarda mas de un minuto:
- decirle "Estas exagerando, dime algo mas conciso"
c) Cuanto tardaria una persona que habla un 30% mas rapido
"""
texto = input("Ingresa cualquier texto real: ")
palabras = texto.split(" ")

if float(cantidad) / 2 < 60:
    print(f'El texto es: {texto} \na)\n- Tardarias un total de {((float(len(palabras))) / 2):.2f} segundos en terminar tu texto \n- Dijiste un total de {len(palabras)} palabras. \nb)\n- Una persona que habla un 30% mas rapido lo diria en: {(((float(len(palabras))  )/ 2)*30/100):.2f} segundos')
else:
     print(f'El texto es: {texto} \nc)\n- Estas exagerando dime algo mas conciso')

