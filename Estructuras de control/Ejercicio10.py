"""
Datos de entrada
chelines austriacos-->ca-->float
dragmas griegos-->dg-->float
pesetas-->ps-->float
Datos de salida
chelineas a pesetas-->caps-->float
dragmas a francos franceses-->dgff-->float
pesetas a dólares-->psdl-->float
pesetas a liras italianas-->pslt-->float
"""
#Entradas
ca=float(input("Digite la cantidad de chelines austriacos "))
dg=float(input("Digite la cantidad de dragmas griegos "))
ps=float(input("Digite la cantidad de pesetas "))
#Caja negra
caps=(ca*956.871)/100
dgff=(((dg*88.607)/100)/20.110)
psdl=(ps/122.49)
psli=(ps*100)/9.289
