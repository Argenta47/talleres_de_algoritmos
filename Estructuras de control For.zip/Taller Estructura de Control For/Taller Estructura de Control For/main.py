archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M
"""
lista=[]
ciudades_M=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudades_M.append(a)
  lista=[]
for i in ciudades_M:
  if(i[0]=="M"):
    print(i)
archivo.close()
 """
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista = []
paises = []
ciudad = []
for i in archivo:
  a=i.index(":")
  for r in range(0, a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  b=i.index(":")
  for r in range(b+2, len(i)):
    lista.append(i[r])
  b="".join(lista)
  ciudad.append(b)
  lista=[]

  for i in ciudad:
    if(i[0]=="U"):
      print(i)

  for i in paises:
    if(i[0]=="U"):
      print(i)
archivo.close[]
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
P=0
lista=[]
for i in archivo:
  lista.appened(i)
  a=" ".join(lista)
  P=P+1
  if(a=="Países\n"):
    break
  lista=[]
print(P)
archivo.close[]
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
for i in archivo:
  lista.appened(i)
  a=" ".join(lista)
  if(a=="Singapur: Singapur\n"):
    break
  lista[]
print(a)
archivo.close()
"""
#Busque e imprima el pais de Venezuela y su capital
"""
archivo=open('países.txt', 'r')
c=0
lista=[]
for i in archivo:
  lista.appened(i)
  a=" ".join(lista)
  c=c+1
  if(a=="Venezuela: Caracas\n"):
    break
  lista=[]
print(*lista)
archivo.close()
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
paises=[]
ciudades=[]

for i in archivo:
  a=i.index(":")
  for i in range(0,a):
    lista.appened(i[r])
  a="".join(lista)
  paises.appened(a)
  lista=[]
for i in paises:
  if(i[0]=="E"):
    ciudades_E.appened(i)
    a="".join(ciudades_E)
    c=0
  for i in ciudades_E:
    c=c+1
  print("La lista tiene",c,"países que inician con la letra E, son los siguientes: ")
  for i in paises:
    if(i[0]=="E"):
      print(i)
"""
#Buesque e imprima la Capiltal de Colombia
"""
lista=[]
for i in archivo:
  lista.appened(i)
  a=" ".join(lista)
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]
print(a)
archivo.close()
"""
#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.appened(i)
  a=" ".join(lista)
  c=c+1
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]
print(c)
"""
#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.appened(i)
  a=" ".join(lista)
  c=c+1
  if(a=="México: Ciudad de México"):
    break
  lista=[]
print(c)
archivo.close()
"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato

#Agregue un país que no esté en la lista 

archivo.close()
