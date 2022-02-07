"""
Datos de entrada
presupuesto total-->p-->int
Datos de salida
presupuesto ginecología-->pg-->float
presupuesto traumatología-->pt-->float
presupuestp pediatría-->pp-->float
"""
#Entradas
p=int(input("Digite el prespuesto anual del hospital "))
#Caja negra
pg=p*0.4
pt=p*0.3
pp=p*0.3
#Salidas
print=(f"El presupuesto para ginecología es de {pg}")
print=(f"El presupuesto para traumatología es de {pt}")
print=(f"El presupuesto para pediatría es de {pp}")
