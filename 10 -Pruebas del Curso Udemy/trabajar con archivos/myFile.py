"""myFile = open("fruits.txt")

content = myFile.read()
myFile.close()
#print(myFile.read())"""

""" with open("./files/fruits.txt") as myFile:
    content = myFile.read()

print(content)

with open("./files/vegetables.txt", "w") as myFile:
    myFile.write("tomat\nCucumber\nOnion")
    
with open("./files/vegetables.txt", "a") as myFile:
    myFile.write("tomat\nCucumber\nOnion") """


with open("./files/vegetables.txt", "a+") as myFile:
    myFile.write("tomat\nCucumber\nOnion")
    myFile.seek(0)
    content = myFile.read()

print(content)
