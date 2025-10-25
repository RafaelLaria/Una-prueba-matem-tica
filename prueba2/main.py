from punto import Punto
from rectangulo import Rectangulo

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

print(A.cuadrante())
print(C.cuadrante())
print(D.cuadrante())

print(f"El vector AB es: {A.vector(B)}")
print(f"El vector BA es: {B.vector(A)}")

print(f"La distancia entre A y B es: {A.distancia(B)} unidades")

rect = Rectangulo(A,B)
print(f"La base del rectángulo es: {rect.base()} unidades")
print(f"La altura del rectángulo es: {rect.altura()} unidades")
print(f"El área del rectángulo es: {rect.area()} unidades cuadradas")