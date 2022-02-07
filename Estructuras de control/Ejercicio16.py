"""
Datos de entrada
precio galon-->p-->float
galones tanqueados-->gt-->float
Datos de salida
costo tanqueada-->cop-->float
"""
#Entradas
gt=float(input("Digite los galones que se tanquearon al carro "))
#Caja negra
p=3.785*50000
cop=gt*p
#Salidas
print(f"Al cliente se le deben cobrar {cop}"+"$")
