users = {
 "iperurena": {
 "nombre": "Iñaki",
 "apellido": "Perurena",
 "password": "123123"
 },
 "fmuguruza": {
 "nombre": "Fermín",
 "apellido": "Muguruza",
 "password": "654321"
 },
 "aolaizola": {
 "nombre": "Aimar",
 "apellido": "Olaizola",
 "password": "123456"
 }
 }

attempts = 0

def tryLogin():
  print("")
  user = input("Usuario: ")
  password = str(input("Password: "))
  if(user in users):
    if(users[user]["password"] == password):
      global userLogged
      userLogged = users[user]
      return True
  return False

print("Pantalla de Login")
while(True):
  if(tryLogin()):
    print("Usuario logeado correctamente")
    print("Bienvenido, "+userLogged["nombre"]+" "+userLogged["apellido"])
    break
  attempts = attempts + 1
  if(attempts >= 3):
    print("")
    print("Itentos acabados")
    break
  else:
    print("¡Credenciales incorrectas!")
  
  