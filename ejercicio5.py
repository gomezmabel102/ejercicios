num1 = int(input("Ingresa un número:")) 
num2 = int(input("Ingresa otro número:")) 
texto = ''
if num1> num2 :
    texto = f"{num1} es mayor que {num2}"
elif num1 < num2:
    texto = f"{num2} es mayor que {num1}"
else :
    texto = f"{num2} y {num1} son iguales"

print(texto)