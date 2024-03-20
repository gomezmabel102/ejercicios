edad = 16
tiene_licencia = False

#edad = int(input("ingresa tu edad:"))

if edad >= 18:
  if tiene_licencia == True:
    print("Puede conducir")
  else:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
  print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")