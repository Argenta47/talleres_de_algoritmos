estudiantes = {}

counter = 1

def getGrade():
  print("")
  name = input("Nombre: ")
  grade = input("Nota: ")
  estudiantes.update({name: grade})

def printGrades():
  print("")
  print(estudiantes)

while(True):
  print("")
  print("Datos del estudiante "+str(counter))
  getGrade()
  if(counter >= 3):
    break
  counter = counter + 1

printGrades()