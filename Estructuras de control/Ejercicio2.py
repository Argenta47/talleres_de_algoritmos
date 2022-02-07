"""
Datos de entrada
dinero-->d-->int
porcentaje ganancia-->p-->int
Datos de salida
total-->t-->int
"""
#Entradas
d=int(input("Ingrese el valor: "))
#Caja negra
p=d*0.02
t=p+d
#Salidas
print(f"Su saldo pasado el mes es: {int(t)}")
