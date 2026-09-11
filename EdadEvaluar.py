"""
Evaluar si la edad del usuario capturado en el frontend permite su inclusión en el modelo de riesgo crediticio; debes garantizar que sea estrictamente mayor o igual a 18 y menor a 65 años.
"""

edad = 23

if edad >= 18 and edad < 65:
    print("Acceso garantizado")
else:
    print("Acceso denegado")
