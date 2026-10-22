"""
Recrear la serie de fibonacci entre un rango determinado
"""

cache = {0: 0, 1: 1}

def fibonacci_of(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return cache[n]
    
inicio = int(input("Ingresa el valor de inicio: "))
fin = int(input("Ingresa el valor de fin: "))
serie = [fibonacci_of(n) for n in range(inicio, fin + 1)]

print(f"Tu serie es: {serie}")
