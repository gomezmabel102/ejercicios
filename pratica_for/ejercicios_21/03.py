#ejercicio1
alumnos_clase = ["Maria", "jose","Carlos", "Martina", "isabel","Tomas", "Daniela"]

for nombre in alumnos_clase:
   print (f"hola{nombre}")

#ejercicio2
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4] 
suma_numeros = 0 

for numeros in lista_numeros:
    suma_numeros += numeros

print ("suma_numeros es:", {suma_numeros})

#ejercicio3
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4] 
suma_pares = 0
suma_impares= 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares+=numero
        print("la suma de numeros pares es:",{suma_pares})

for numero in lista_numeros:
    if numero % 2 == 1:
        suma_impares+=numero
        print("la suma de numeros impares es:",{suma_impares})

