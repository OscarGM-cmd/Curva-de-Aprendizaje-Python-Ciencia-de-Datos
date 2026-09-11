"""
Validar el código de respuesta HTTP de nuestra API externa de recolección de telemetría: si es 200, proceder con la extracción; si es 404, registrar un evento de advertencia en el log; si es 500, encolar un reintento con backoff exponencial.
"""

#Simulacion de que el codigo de respuesta HTTP solicitado fue de los 3 casos
codigo = input("Ingresa codigo de respuesta: ")

if  codigo == 200:
    print("Procediendo con la extraccion...")
    # Codigo referente
elif codigo == 404:
    print("Advertencia")
elif codigo == 500:
    print("Iniciando intento backoff...")
else:
    print("Fallo el sistema")