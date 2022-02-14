"""
Datos de entrada
fecha de nacimiento-->f-->date
Datos de salida
signo del zodiaco-->z-->str
"""

import datetime 
x = datetime.datetime.now()
mes_actual=int(x.strftime("%m"))
año_actual=int(x.strftime("%Y"))
dia_actual=int(x.strftime("%d"))
f=input("Digite en este formato: 'dd/mm/yy' : ")
day, month, year = f.split('/')
dia_nacimiento=int(day)
mes_nacimiento=int(month)
año_nacimiento=int(year)
años=0
if(dia_actual>=dia_nacimiento and mes_actual>=mes_nacimiento):
    años=año_actual-año_nacimiento
else:
    años=año_actual-año_nacimiento-1
print(años)
