"""
Datos de entrada
nivel de hemoglobina-->NH-->float
edad-->E-->int
sexo-->S-->str
Datos de salida
resultado de anemia-->R-->str
"""

NH=float(input("Ingrese el nivel de hemoglobina: "))
TE=float(input("Edad en días digite 1, edad en meses digite 2, edad en años digite 3: "))
E=int(input("Ingrese la edad del paciente: "))
S=str(input("Ingrese el sexo en minusculas: "))


if(TE==1 and E>0 and E<=60 and NH<=13):
 print("Resultado para anemia: Positivo")
else:
  (TE==1 and E>0 and E<=60 and NH>13 and NH<26)
  print("Resultado para anemia: Negativo")


if(TE==2 and E>1 and E<=6 and NH<=10):
  print("Resultado para anemia: Positivo")
else:
  (TE==2 and E>1 and E<=6 and NH>10 and NH<18)
  print("Resultado para anemia: Negativo")


if(TE==2 and E>6 and E<=12 and NH<=11):
  print("Resultado para anemia: Positivo")
else:
  (TE==2 and E>6 and E<=12 and NH>11 and NH<15)
  print("Resultado para anemia:Negativo")

if(TE==3 and E>1 and E<=5 and NH<=11.5):
  print("Resultado para anemia: Positivo")
else:
  (TE==3 and E>1 and E<=5 and NH>11.5 and NH<15)
  print("Resultado para anemia: Negativo")

if(TE==3 and E>5 and E<=10 and NH<=12.6):
  print("Resultado para anemia: Positivo")
else:
  (TE==3 and E>5 and E<=10 and NH>12.6 and NH<15.5)
  print("Resultado para anemia: Negativo")


if(TE==3 and E>10 and E<=15 and NH<=13):
  print("Resultado para anemia: Positivo")
else:
  (TE==3 and E>10 and E<=15 and NH>13 and NH<15.5)
  print("Resultado para anemia: Negativo")


if(TE==3 and S=="femenino" and E>15 and NH<=12):
  print("Resultado para anemia: Positivo")
else:
  (TE==3 and S=="femenino" and E>15 and NH>12 and NH<16)
  print("Resultado para anemia: Negativo")  

if(TE==3 and S=="masculino" and E>15 and NH<=14):
  print("Resultado para anemia: Positivo")
else:
  (TE==3 and S=="masculino" and E>15 and NH>14 and NH<18)
  print("Resultado para anemia: Negativo")
  