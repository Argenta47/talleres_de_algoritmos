"""
Datos de entrada
distancia recorrida-->d-->float
Datos de salida
precio a pagar-->p-->float
"""

d=float(input("Digite la distancia recorrida en km "))

if(d<=300):
    p=50000
    print(f"Precio a pagar: {p}")
elif(d>300 and d<1000):
    p=(70000+(d-300)*30000)
    print(f"Precio a pagar: {p}")
elif(d>300 and d>1000):
    p=(150000+(d-300)*9000)
    print(f"Precio a pagar: {p}")
    