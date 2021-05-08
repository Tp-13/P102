f = open("Text.txt")
fileLines = f.readlines()
for line in fileLines:
    print(line)

found = False
introString = input("Enter Your String: ")
searchString = input("Enter The Word You Want to Search: ")
words = introString.split()
for word in words:
    if word == searchString:
        found = True

if found == True:
    print("Word Found!")
else:
    print("Not Found!")

"""def greet(name):
    print("Hello " + name + ", how are you?")

greet("Tanush")"""