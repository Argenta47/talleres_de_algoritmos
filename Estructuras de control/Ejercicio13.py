"""
Datos de entrada
billetes de 50000-->n1-->int
billetes de 20000-->n2-->int
billetes de 10000-->n3-->int
billetes de 5000-->n4-->int
billetes de 2000-->n5-->int
billetes de 1000-->n6-->int
billetes de 500-->n7-->int
billetes de 100-->n8-->int
total de 50.000-->t1-->int
total de 20.000-->t2-->int
total de 10.000-->t3-->int
total de 5.000-->t4-->int
total de 2.000-->t5-->int
total de 1.000-->t6-->int
total de 500-->t7-->int
total de 100-->t8-->int
Datos de salida
total dinero-->t-->int
"""
#Entradas
n1=int(input("Digite el número de billetes de 50.000 "))
n2=int(input("Digite el número de biiletes de 20.000 "))
n3=int(input("Digite el número de biiletes de 10.000 "))
n4=int(input("Digite el número de biiletes de 5.000 "))
n5=int(input("Digite el número de biiletes de 2.000 "))
n6=int(input("Digite el número de biiletes de 1.000 "))
n7=int(input("Digite el número de biiletes de 500 "))
n8=int(input("Digite el número de biiletes de 100 "))
#Caja negra
t1=n1+50000
t2=n2*20000
t3=n3*10000
t4=n4*5000
t5=n5*2000
t6=n6*1000
t7=n7*500
t8=n8*100
t=t1+t2+t3+t4+t5+t6+t7+t8
#Salidas
print(f"El total de dinero que tiene es banco es de {t}")
