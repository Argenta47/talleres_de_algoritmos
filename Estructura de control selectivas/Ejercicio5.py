"""
Datos de entrada
importe departamento a-->a-->float
importe departamento b-->b-->float
importe departamento c-->c-->float
importe global de ventas-->vt-->float
salario-->s-->float
Datos de salida
salario neto-->sn-->float
"""
#Entradas
a=float(input("Digite el importe del departamento a "))
b=float(input("Digite el importe del departamento b "))
c=float(input("Digite el importe del departamento c "))
s=float(input("Digite el salario "))
#Caja negra
vt=a+b+c
p=vt*0.33
if(a>p):
    sn=(s*0.2)+s
    