# simple loop in combination with selection statement
for i in range (10):
    print(i, end=" ") # print the number we are on
    if i % 2 == 0: # if the number is divisible by 2
        print("even")
    else: # if not divisible by 2
        print("odd")
        # why can we use ELSE here?

        

string = "TextInRandomOrder"
print("\n%s" % string)
set = set()
set.add("T")
set.add("I")
set.add("R")
set.add("O")
print(*set, sep = ", ", end = "\n")
counter = 0
for char in string:
    if char in set: # if the character we are on is in a 
        print("Found %s" % char)
        counter += 1 # add 1 to the total amount found
print("Found %d matching characters in total" % counter)