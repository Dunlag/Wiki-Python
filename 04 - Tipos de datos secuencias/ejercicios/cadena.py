cadena = "informatica"

for c in cadena:
    print(c)
    
"a" in cadena

"b" in cadena

"a" not in cadena

cadena[0]

cadena[2:5]

cadena[2:7:2]

cadena[::-1]

#las cadenas de caracteres son inmutables

cadena[2]="g"

cadena = cadena.upper()	

#metodos principales de cadenas

cad = "hola, como estas?"
cad.capitalize()

cad = "hola mundo"
cad.upper();
cad.lower();
cad.swapcase();
cad = "hola mundo"
cad.title()

cad= "bienvenido a mi aplicacion"
cad.count("a")
cad.count("a",16)
cad.count("a",10,16)

cad.find("mi")
cad.find("hola")

cad.startswith("b")
cad.startswith("bien",13)
cad.endswith("cion")

cad.replace("a", "U")

cad = "bienvenido a mi aplicacion"
cad.strip()

hora = "12:23:12"
hora.split(":")
