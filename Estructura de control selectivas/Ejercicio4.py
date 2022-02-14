"""
Datos de entrada
monto de la compra-->m-->float
Datos de salida
fondos de la empresa-->f-->float
pago a crédito-->pc-->float
pago intereses-->pi-->float
prestamo del banco-->pb-->float
"""
#Entradas
m=float(input("Digite la cantidad del monto de la compra "))
#Caja negra
if(m>5000000):
    f=m*0.55
    pb=m*0.3
    pc=m*0.15
    pi=(pc*0.2)+pc
elif(m<=5000000):
    f=m*0.7
    pc=m*0.3
    pi=(pc*0.2)+pc
    pb="No se necesita"
#Salidas
print(f"Inversión por fondos de la empresa: {f}")
print(f"Cantidad a pagar a crédito: {pc}")
print(f"Cantidad a pagar por intereses: {pi}")
print(f"Cantidad prestada del banco: {pb}")
