ingreso_mensual = 81000
gasto_mensual = 80000

#Ifs anidados y elif
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deuda")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bastante bien")
    else:
        print("Corrobora si te alcanza realmente")


if ingreso_mensual > 100000:
    print("Estas bien economicamente en cualquier parte del mundo")
elif ingreso_mensual > 1000:
    print("Estas bien economica en latinoamerica")
else:
    print("Dinero insuficiente")