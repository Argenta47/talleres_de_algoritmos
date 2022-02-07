"""
Datos de entrada
edad_uno-->e_uno-->int
edad_dos-->e_dos-->int
edad_tres-->e_tres-->int
Datos de salida
promedio-->p-->float
"""
#Entradas
e_uno=int(input("Digite edad uno: "))
e_dos=int(input("Digite edad dos: "))
e_tres=int(input("Digite edad tres: "))
#Caja negra
p=(e_uno+e_dos+e_tres)/3#float
#Saidas
print(f"El promedio es: {p}")
