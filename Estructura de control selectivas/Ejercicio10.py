"""
Datos de entrada
categoría-->c-->int
salario bruto-->sb-->float
Datos de salida
aumento-->a-->float
nuevo salario-->ns-->float
"""

sb=float(input("Digite el salario bruto "))

if(sb==5000000):
    a=sb*0.1
    ns=sb+a
    print("La categoría es 1, y su nuevo salario es de $"+str(ns))
elif(sb==4300000):
    a=sb*0.15
    ns=sb+a
    print("La categoría es 2, y el nuevo salario es de $"+str(ns))
elif(sb==3600000):
    a=sb*0.2
    ns=sb+a
    print("La categoría es 3, y el nuevo salario es de $"+str(ns))
elif(sb==2000000):
    a=sb*0.4
    ns=sb+a
    print("La categoría es 4, y el nuevo salario es de $"+str(ns))
elif(sb==900000):
    a=sb*0.6
    ns=sb+a
    print("La categoría es 5, y el nuevo salario es de $"+str(ns))
