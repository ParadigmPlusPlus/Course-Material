# simple loop with known amount of repetition
for i in range (10): # from 0 to 9
    print(i, end=", ")
print()

# loop from hig to low
for i in range (10, 0, -1): # from 10 to 1
    print(i, end=", ")
print()

# go through each character of a string
string = "String"
for char in string:
    print(char, end=" ")
print()

# go through each character of string from BACK TO FRONT
for i in range (len(string) - 1, -1, -1):
    print(string[i], end=" ")
print()

# FOR loop stop at the end of the cycle before the condition is met