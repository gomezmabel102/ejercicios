habla_ingles = True 
sabe_python = False 
msj = ""

if habla_ingles:
    if sabe_python:
        msj= "Cumples con los requisitos para postularte" 
    else:
        msj = "Para postularte, necesitas saber programar en Python"  
elif sabe_python:
    msj = "Para postularte, necesitas tener conocimientos de inglés"
else:
    msj = "Para postularte, necesitas saber programar en Python y tener conocimientos de inglés" 
print(msj)