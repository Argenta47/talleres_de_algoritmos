"""
Datos de entrada
temperatura-->t-->float
Datos de salida
deporte-->d-->str
"""

t=float(input("Ingrese la temperatura "))

if(t>85):
  d="Natación"
  print(d)
if(t>70 and t<=85):
  d="Tenis"
  print(d)
if(t>32 and t<=70):
  d="Golf"
  print(d)
if(t>10 and t<=32):
  d="Esquí"
  print(d)
if(t<=10):
  d="Marcha"
  print(d)
  