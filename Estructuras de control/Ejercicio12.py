"""
Datos de entrada
-matemáticas
exámen final-->efm-->int
tarea 1-->t1m-->int
tarea 2-->t2m-->int
tarea 3-->t3m-->int
porcentaje exámen final-->pefm-->float
promedio tareas-->ptm-->float
porcentaje tareas-->pptm-->float
-fisíca
exámen final-->eff-->int
tarea 1-->t1f-->int
tarea 2-->t2f-->int
porcentaje exámen final-->peff-->float
promedio tareas-->ptf-->float
porcentaje tareas-->pptf-->float
-química
exámen final-->efq-->int
tarea 1-->t1q-->int
tarea 2-->t2q-->int
tarea 3-->t3q-->int
porcentaje exámen final-->pefq-->float
promedio tareas-->ptq-->float
porcentaje tareas-->pptq-->float
Datos de salida
calificación final matemáticas-->cfm-->float
calificación final física-->cff-->float
calificación final química-->cfq-->float
promedio de las tres materias-->pm-->float
"""
#Entradas
input("Matemáticas")
efm=int(input("Digite la calificación del exámen final "))
t1m=int(input("Digite la calificación de la tarea 1 "))
t2m=int(input("Digite la calificación de la tarea 2 "))
t3m=int(input("Digite la calificación de la tarea 3 "))
input("Física")
eff=int(input("Digite la calificación del exámen final "))
t1f=int(input("Digite la calificación de la tarea 1 "))
t2f=int(input("Digite la calificación de la tarea 2 "))
input("Química")
efq=int(input("Digite la calificación del exámen final "))
t1q=int(input("Digite la calificación de la tarea 1 "))
t2q=int(input("Digite la calificación de la tarea 2 "))
t3q=int(input("Digite la calificación de la tarea 3 "))
#Caja negra
pefm=efm*0.9
ptm=(t1m+t2m+t3m)/3
pptm=ptm*0.1
cfm=pefm+pptm
peff=eff*0.8
ptf=(t1f+t2f)/2
pptf=ptf*0.2
cff=peff+pptf
pefq=efq*0.85
ptq=(t1q+t2q+t3q)/3
pptq=ptq*0.15
cfq=pefq+pptq
pm=(cfm+cff+cfq)/3
#Salidas
print(f"La calificación final de matemáticas es: {cfm}")
print(f"La calificación final de física es: {cff}")
print(f"La calificación final de química es: {cfq}")
print(f"El promedio de las tres materias es: {pm}")
