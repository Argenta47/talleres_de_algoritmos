"""
Datos de entrada
precio hora-->ph-->float
descuento-->d-->float
salario base-->s-->float
horas trabajadas-->h-->float
Datos de salida
salario neto-->sn-->float
"""
#Entradas
h=float(input("Digite las horas trabajadas "))
ph=float(input("Digite el precio por hora "))
#Caja negra
s=h*ph
d=s*0.2
sn=s-d
#Salidas
print(f"El salario neto es: {sn}")
