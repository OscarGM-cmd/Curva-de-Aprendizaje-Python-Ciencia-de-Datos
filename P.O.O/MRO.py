class A:
    def hablar(self):
        print("Hola desde A")

class F:
    def hablar(self):
        print("Hola desde F")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(F):
    def hablar(self):
        print("Hola desde C")

# Funciona como un arbol, por ramificacion
# La clase D si no tuviera una funcion en su bloque de hablar, jerarquicamente despues comprobara en B y despues A
# en caso que ni D,B,A no tengan regresara al inicio e ira a C y en caso de que no tenga la funcion C 
# ira hasta F, D -> B -> A -> C -> F
# en caso que heren una misma funcion 2 clases el caso seria: D -> B -> C -> A
class D(B,C):
    def hablar(self):
        print("Hola desde D")

d = D()
F.hablar(d)
print(D.mro())