numbersArray = [12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
numbersAmount = {}

def analizeArray():
  for number in numbersArray:
    addNumber(number)

def addNumber(newNumber):
  if(newNumber in numbersAmount):
    numbersAmount.update({newNumber: numbersAmount[newNumber]+1})
  else:
    numbersAmount.update({newNumber: 1})
  
def showDictionary():
  print(numbersAmount)

print("Contador de numeros")
print("(Modifica la lista para ver los cambios)")
print("")
analizeArray()
showDictionary()
