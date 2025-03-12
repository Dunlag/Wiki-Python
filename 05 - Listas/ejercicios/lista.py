lista1 = []
print (type(lista1))
lista2=[1,"a",True]
lista=[1,2,3,4,5,6]
for num in lista:
    print(num)

lista2=["a","b","c","d","e"]
for num,letra in zip(lista,lista2):
    print(num," ",letra)
    
7 in lista

lista + [6,7,8]

lista[2:4]
lista[2:5:2]
lista[::-1]

max(lista)
min(lista)
sum(lista)

lista = [3,7,1,9,12,34,0]
sorted(lista)
sorted(lista, reverse=True)

tabla = [[1,2,3],[4,5,6]]
for fila in tabla:
    for elem in fila:
        print(elem)

#las listas son mutables, se modifican las listas
lista5 = [1,2,3]        
lista5[1]=100 
print(lista5)

lista5.append(5)

lista6 = lista5
lista5.append(100)
print(lista6)
#lista copiar pero sin modificar la lista anterior
lista7 = lista6[:]
print(lista7)
lista6.append(44)
print(lista6)
print(lista7)

#principales metodos de las listas
lista = [1,2,3]
lista.append(4)
lista2=[5,6]
lista.extend(lista2)
print(lista)
lista.insert(1,100)
print(lista)
lista.pop()
print(lista)
lista.pop(1)
print(lista)
lista.remove(3)
print(lista)
lista.reverse()
print(lista)
lista.sort()
lista.sort(reverse=True)
#tambien funciona con palabras
lista.count(5)
lista.index(5)

