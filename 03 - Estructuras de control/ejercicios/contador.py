cont = 0 
for var in range(1,4):
    num = int(input("Dime un numero: "))
    if num % 2 == 0:
        cont = cont + 1
if cont == 1:
    print ("has introducido un unico numero par")
else:
    print("has introducido",cont,"numeros pares")