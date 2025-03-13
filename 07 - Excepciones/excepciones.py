while True:
    try:
        x = int(input("Dime un numero: "))
        break
    except ValueError:
        print("Debes introducir un numero")
    else: 
        print("Se ha producido otro error")
    finally:
        print("Se ha finalizado el programa")
