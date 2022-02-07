"""
Entradas
sueldo base-->s-->int
venta1-->v1-->int
venta2-->v2-->int
venta3-->v3-->int
porcentaje1-->p1-->float
porcentaje2-->p2-->float
porcentaje3-->p3-->float
comisiones-->c-->int
Salidas
total-->t-->int
"""
#Entradas
s=int(input("Digite el sueldo base "))
v1=int(input("Digite el valor de la venta 1 "))
v2=int(input("Digite el valor de la venta 2 "))
v3=int(input("Digite el valor de la venta 3 "))
#Caja negra
p1=v1*0.1
p2=v2*0.1
p3=v3*0.1
c=p1+p2+p3
t=s+c
#Salidas
print(f"Sus ingresos toales son de {int(t)}")
