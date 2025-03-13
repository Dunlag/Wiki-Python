diccionario = {'one':1, 'two':2, 'three':3}
print (diccionario)
print(type(diccionario))
print(diccionario['two'])

dict1={}
dict1["nombre"]="jose"
dict1["edad"]=20
print(dict1)
print(len(dict1))

del diccionario["one"]
print(diccionario)

#metodos principales de un diccionario

dict1.clear()
print(dict1)
dict1 = {'one':1, 'two':2, 'three':3}
dict2 = {'four':4, 'five':5, 'six':6}

dict1.update(dict2)
print(dict1)

print (dict1.get("one"))
print (dict1.get("ones","no existe"))

dict1.pop("one")
dict1.pop("seven","no existe")

for clave in dict1.keys():
    print(clave)

for clave in dict1.values():
    print(clave)

for clave,valor in dict1.items():
    print(clave,valor)