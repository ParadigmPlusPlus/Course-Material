string = "String"
userInput = input()
while userInput.lower() != "end":
    print(string[int(userInput)])
    userInput = input()

string = "This is just a string used to test substring"
print(string[-2:])

string = "A--------------------------z"
string1 = string[0].lower() + string[1:]
string2 = string1[0:len(string1) - 2] + string1[len(string1) - 1].upper()
print(string2)