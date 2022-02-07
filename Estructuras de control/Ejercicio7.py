"""
Datos de entrada
metro-->m-->float
pulgadas-->pg-->float
pies-->ft-->float
Datos de salida
distancia pulgadas-->din-->float
distancia pies-->dft-->float
"""
#Entradas
m=float(input("Digite la distancia "))
#Caja negra
pg=m*39.37
ft=pg/12
#salidas
print(f"La distancia en pulgadas es {pg}")
print(f"La distancia en pies es {ft}")
