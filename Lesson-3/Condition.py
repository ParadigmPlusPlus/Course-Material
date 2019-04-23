if 5 > 4:
    print("5 > 4")

a = 5
b = 5
if a == b: # replace == with <, > , <=, >=, !=, change value of 'a' and 'b'
    print("a > b")

a = 5
b = 4
if a == b + 1:
    print("a = b + 1")
if a > b:
    print("a > b")

# skip all of the other conditions as soon as one is met
if a == b + 1:
    print("a = b + 1")
elif a > b:
    print("a > b")

# categorize remaining condition as one
if a == b:
    print("a = b")
else:
    print("a does not equal to b")

# multiple requirments for one condition
c = 5
d = 5
name = input()
if c == d and name == "M":
    print("All condition satisfied")
elif c == d or name == "M":
    print("Only one condition is satisfied")
else:
    print("At least one of the condition is not satisfied")
