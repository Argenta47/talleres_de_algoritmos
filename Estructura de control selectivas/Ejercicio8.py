"""
Datos de entrada
P-->p-->int
Q-->q-->int
Datos de salida
mensaje-->m-->float
"""

p=int(input("Ingrese el valor de p "))
q=int(input("Ingrese el valor de q "))

if(p**3+q**4-2*p**2>680):
    print(str(p)+" y "+ str(q)+" satisfacen la expresión")
else:
    (p**3+q**4-2*p**2<680)
    print(str(p)+" y "+ str(q)+" no satisfacen la expresión")
