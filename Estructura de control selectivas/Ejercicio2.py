"""
Datos de entrada
sueldo bruto-->s-->int
Datos de salida
nuevo sueldo-->ns-->float
"""
#Entradas
s=int(input("Digite su sueldo "))
#Caja negra
if(s<900000):
    ns=(s*0.15)+s
elif(s>=900000):
    ns=(s*0.12)+s
#salidas
print(f"Su nuevo sueldo es de: {ns}")
