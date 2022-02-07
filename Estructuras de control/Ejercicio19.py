"""
Datos de entrada
naranjas compradas-->x-->int
valor docena-->y-->int
venta de naranjas-->p-->float
Datos de salida
total inversión-->ti-->int
ganacias-->g-->float
porcentje de ganancias-->pg-->float
"""
#Entradas
x=int(input("Digite el número de naranjas compradas "))
y=int(input("Digite el valor de la docena "))
p=float(input("Digite la venta de naranjas "))
#Caja negra
ti=(x/12)*y
g=p-ti
pg=(g*100)/ti
#Salidas
print(f"El procentaje de ganancias es: {pg}"+"%")
