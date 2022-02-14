"""
Datos de entrada
capital-->c-->float
porcentaje de interés-->pi-->float
Datos de salida
dinero generado-->d-->float
dinero total-->dt-->float
"""
#Entradas
c=float(input("Digite el capital a invertir "))
pi=float(input("Digite el porcentaje de interés "))
#Caja negra
d=c*pi
intereses=""
if(d>100000):
    intereses="Reinvertir"
elif(d<=100000):
    intereses="No reinvertir"
dt=c+d
#Salidas
print(f"El dinero generado por los intereses es: {d}")
print(f"{intereses}")
