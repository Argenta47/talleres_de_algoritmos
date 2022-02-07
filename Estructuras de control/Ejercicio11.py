"""
Datos de entrada
trabajador-->nombre-->str
horas trabajadas-->ht-->float
precio por hora-->ph-->float
horas extra-->hx-->float
precio hora extra-->phx-->float
Deducciones-->d-->float
paro forzoso->pf-->float
política habitacional-->polh-->float
caja de ahorro-->ch-->float
Asignaciones-->a-->float
actualización académica-->aa-->int
cantidad hijos-->ca-->int
asignación hijo-->ah-->int
pago por hijo-->pa-->int
prima hogar-->ap-->int
Salidas
sueldo normal-->s-->float
incremento hora extra-->ihx-->float
pago hora extra-->phx-->float
sueldo base-->sb-->float
sueldo de diciembre-->sd-->float
"""
#Entradas
nombre=str(input("Ingrese su nombre "))
ht=float(input("Digite las horas trabajadas "))
ph=float(input("Digite el precio por hora "))
hx=float(input("Digite las horas extra trabajadas "))
pf=float(input("Digite el porcentaje por paro forzoso "))
polh=float(input("Digite el porcentaje por política habitacional "))
ch=float(input("Digite el porcentaje por caja de ahorro "))
ca=int(input("Digite el número de hijos que tiene "))
aa=int(input("Digite la asignación de actuaización académica "))
ah=int(input("Digite la asignación por hijo "))
ap=int(input("Digite la asignación de la prima "))
#Caja negra
phx=(ph*0.25)+ph
s=ht*ph
ihx=hx*phx
sb=s+ihx
d=sb*(pf+polh+ch)
pa=ah*ca
a=aa+pa+ap
sd=(sb+a)-d
#Salidas
print(f"El total de asignaciones es: {a}")
print(f"El total de deduciones es: {d}")
print(nombre,(", su saldo neta para el mes de diciembre es: "+str(sd)))
