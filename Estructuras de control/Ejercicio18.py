"""
Datos de entrada
capital-->c-->int
tiempo-->t-->float
tasa-->ts-->float
Datos de salida
intereses-->i-->float
porcentaje préstamo-->pp-->float
"""
#Entradas
c=int(input("Digite el capital "))
t=float(input("Digite el tiempo de cobro "))
ts=float(input("Digite la tasa de interés "))
#Caja negra
i=(c*t*ts)/100
pp=ts*12
#Salidas
print(f"El interés anual cobrado es de {pp}"+"%")
