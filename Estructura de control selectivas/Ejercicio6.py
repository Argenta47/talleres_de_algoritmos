"""
Datos de entrada
número a-->a-->int
número b-->b-->int
número c-->c-->int
número d-->d-->int
número-->n-->int
Datos de salida
redondeo-->r-->int
"""
a = (input("Igrese la variable A:"))
b = (input("Igrese la variable B:"))
c = (input("Igrese la variable C:"))
d = (input("Igrese la variable D:"))

n=int((a+b+c+d))

c=int(c)
if(c>5):
 r=round(n, -2)
 print(r)

else:
  (c<5)
  r=int((round(n, -2)))
  print(r)
