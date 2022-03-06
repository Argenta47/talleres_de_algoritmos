names = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,
'Maite': 5}

counter = []

def counterUniques():
  for key in names:
    if(names[key] not in counter):
      counter.append(names[key])

def printArray():
  print(counter)

print("Valores unicos")
print("")
counterUniques()
printArray()