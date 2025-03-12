secreto = "hola"
clave = input("Dime la clave: ")
while clave != secreto:
    print("Clave incorrecta!")
    retry = input("¿Quieres volver a intentarlo? (S/N): ")
    if retry.upper()=="N":
        break;
    clave = input("Dime la clave: ")
if clave == secreto:
    print("Bienvenido")
print("Programa terminado")