"""
Datos de entrada
a-->int
b-->int
c-->int
d-->int
Datos de salida
resultado1-->r1-->float
resultado2-->r2-->float
"""
#Entradas
a=int(input("Digite un número entero "))
b=int(input("Digite un número entero "))
c=int(input("Digite un número entero "))
d=int(input("Digite un número entero positivo "))
#Caja negra
if(d==0):
    r1=(a-c)**2
    r2=((a-b)**3)/d
elif(d>0):
    r1=(a-c)**2
    r2=((a-b)**3)/d
#Salidas
print(f"el resultado es {r1}")
print(f"El resultado es {r2}")
