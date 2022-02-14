"""
Datos de entrada
lectura anterior-->l1-->float
lectura actual-->l2-->float
lectura total-->L-->float
Datos de salida
monto a pagar-->m-->float
"""

l1=float(input("Ingrese la lectura anterio: "))
l2=float(input("Ingrese la lectura actual: "))

L=(l1-l2)

if(L>0 and L<=100):
  m=L*4600
  print("Monto a pagar: $"+str(m))
elif(L>101 and L<=300):
 m=L*80000
 print("Monto a pagar: $"+str(m))
elif(L>301 and L<=500):
 m=L*100000
 print("Monto a pagar: $"+str(m))
elif(L>501):
 m=L*120000
 print("Monto a pagar: $"+str(m))
