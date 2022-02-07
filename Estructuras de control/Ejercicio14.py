"""
Datos de entrada
lectura de la factura-->kv-->float
costo kilovatio-->ckv-->float
Datos de salida
monto total-->mt-->float
"""
#Entradas
kv=float(input("Digite el número de kilovoltios consumidos "))
ckv=float(input("Digite el costo del kilovatio "))
#caja negra
mt=kv*ckv
#Salidas
print(f"El monto total de la factura es de {mt}")
