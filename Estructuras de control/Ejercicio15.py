"""
Datos de entrada
precio de venta al público-->pvp-->int
precio pagado-->pp-->float
Datos de salida
descuento aplicado-->d-->float
"""
#Entradas
pvp=int(input("Digite el precio de venta al público "))
pp=float(input("Digite el precio que se pagó "))
#Caja negra
d=((pvp-pp)*100)/pvp
#Salidas
print("El descuento que tuvo fue de "+str(d)+"%")
