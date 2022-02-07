"""
Datos de entrada
lado uno-->l1-->float
lado dos-->l2-->float
lado tres-->l3-->foat
semiperímetro-->sp--Zfloat
Datos de salida
área de triángulo-->a-->float
"""
#Entradas
l1=float(input("Digite el primer lado "))
l2=float(input("Digite el segundo lado "))
l3=float(input("Digite el tercer lado "))
#Caja negra
s=(l1+l2+l3)/2
a=(s*(s-l1)*(s-l2)*(s-l3))**1/2
#Salidas
print(f"El área del triángulo es {a}")
