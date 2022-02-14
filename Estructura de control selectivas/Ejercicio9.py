"""
Datos de entrada
monto de la compra-->m-->float
nombre del cliente-->n-->str
Datos de salida
nombre del cliente-->n-->str
monto de la compra-->m-->float
monto a pagar-->mp-->float
descuento-->d-->float
"""

n=str(input("Ingrese el nombre del cliente "))
m=float(input("Digite el monto de la compra "))

if(m<=50000):
    d=0
    mp=m
    print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d))
elif(m>50000 and m<=100000):
    d=m*0.05
    mp=m-d
    print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d))
elif(m>100000 and m<=700000):
    d=m*0.11
    mp=m-d
    print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d))
elif(m>700000 and m<=1500000):
    d=m*0.18
    mp=m-d
    print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d))
elif(m>1500000):
    d=m*0.25
    mp=m-d
    print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d))
    