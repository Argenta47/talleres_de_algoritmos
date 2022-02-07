"""
Datos de entrada
precio al contado-->pac-->int
precio cuotas-->pc-->float
Datos de salida
porcentaje de recargo-->pr-->float
"""
#Entradas
pac=int(input("Digite el precio a pagar por contado "))
pc=float(input("Digite el precio a pagar por cuotas "))
#Caja negra
pr=(((pc-pac)/12)*100)/pac
#Salidas
print(f"El porcentaje de recargo mensual es del {pr}"+"%")
