#Import lists.
#Tip: bekijk in data.py de structuur van de lists.
from data import hangarList
from data import planeLandedList

#Start program
print("Welkom bij HangarParkeerder3000")
isRunning = True

while isRunning:
  print("-------------------------------------------------")
  print("Deze vliegtuigen wachten om geparkeerd te worden:")

  #!! Loop over planesLanded, print alleen wanneer de hangar 0 is (dat betekent dat het vliegtuig nog _niet_ in een hangar staat).
  for plane in planeLandedList:
      if (plane ["hangar"] == 0):
          print(plane['type']) , (plane['code'])


  #Vraag de gebruiker om een vliegtuigcode in te voeren.
  inputCode = input("\nVoer code in: ")

  #!! Onder deze print: loop over hangars, print alleen wanneer 'occupied' False is.
  print("\nDeze hangars zijn nog vrij:")
  for hangar in hangarList:
      if (hangar["occupied"] == False):
        print(hangar["num"])



  #Vraag de gebruiker om een hangarnummer in te voeren. Blijf de vraag herhalen zolang nog geen geldig nummer is ingevoerd. Sla het nummer op in de variabele "hangar".
  inputHangar = False
  while(inputHangar == False):
    try:
      inputHangar = input("\nVoer nummer in: ")
      inputHangar = int(inputHangar)
    except:
      print("Voer een geldig nummer in!")
      inputHangar = False

  #Tip: pas eventueel deze variabelen aan naar je eigen namen:
  print(f"\nOk, we parkeren {inputCode} in hangar {inputHangar}!\n")

  #Zoek het gekozen vliegtuig, en stel de hangar in op het gekozen nummer.
  for plane in planeLandedList:
    if plane['code'] == inputCode:
      plane['hangar'] = inputHangar
  
  #!! Maak hetzelfde als de for-loop hierboven, maar dan: zoek de gekozen hangar en stel 'occupied' in op True
  for hangar in hangarList:
      if hangar['num'] == inputHangar:
          hangar['occupied'] = True


  #!! Zorg dat het programma stopt als de gebruik een 'X' heeft ingevoerd
  result = input("Druk op enter om door te gaan of typ 'X' om te stoppen...\n")
  if(result == 'X'):
            isRunning = False


  


  #Einde