"""
Entradas
parcial1-->p1-->int
parcial2-->p2-->int
parcial3-->p3-->int
exámen-->e-->int
trabajo-->t-->int
nota parcial-->np-->float
nota exámen-->ne-->float
nota trabajo-->nt-->float
Salidas
calificación final-->c-->int
"""
#Entradas
p1=int(input("Digite la primera nota parcial "))
p2=int(input("Digite la segunda nota parcial "))
p3=int(input("Digite la tercera nota parcial "))
e=int(input("Digite la nota del exámen "))
t=int(input("Digite la nota de trabajo "))
#Caja negra
np=((p1+p2+p3)/3)*0.55
ne=e*0.3
nt=t*0.15
c=np+ne+nt
#Salidas
print(f"S calificación final es: {int(c)}")
