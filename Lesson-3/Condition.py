if 5 > 4:
    print("5 > 4")

a = 5
b = 5
if a == b: # replace == with <, > , <=, >=, !=
    print("a > b")

a = 5
b = 4
if a == b + 1:
    print("a = b + 1")
if a > b:
    print("a > b")

if a == b + 1:
    print("a = b + 1")
elif a > b:
    print("a > b")

if a == b:
    print("a = b")
else:
    print("a does not equal to b")

c = 5
d = 5
name = "M"
if c == d and name == "M":
    print("All condition satisfied")
elif c == d or name == "M":
    print("Only one condition is satisfied")
else:
    print("At least one of the condition is not satisfied")