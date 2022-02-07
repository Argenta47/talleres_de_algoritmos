"""
Entradas
valor compra-->vc-->int
descuento-->d-->float
Salidas
valor con descuento-->vd-->int
"""
#Entradas
vc=int(input("Digite el valor de su compra "))
#Caja negra
d=vc*0.15
vd=vc-d
#Salidas
print(f"Su nuevo saldo es de {int(vd)}")
