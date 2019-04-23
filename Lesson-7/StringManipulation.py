# string work like an array of single character string
string = "String" 
userInput = input()
while userInput.lower() != "end":
    print(string[int(userInput)]) # output whatever index user wanted to output
    userInput = input()

string = "This is just a string used to test substring"
print(string[:4]) # output first 4 characters
print(string[2:5]) # output characters 2 - 4
print(string[-2:])  # output last 2 characters

string = "A--------------------------z"
string1 = string[0].lower() + string[1:] # turn first letter into lowercase
string2 = string1[0:len(string1) - 2] + string1[len(string1) - 1].upper() # turn last letter into uppercase
print(string2)