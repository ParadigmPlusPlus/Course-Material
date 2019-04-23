a = 3
b = 5

print(a + b) # add
print(a - b) # subtract
print(a * b) # multiply
print(a / b) # divide, result is decimal default
print(int(a / b)) # divide, and round to highest integer smaller than the decimal result
print(a % b) # find remainder
c = a + b # assigning value
print(c)

a += b # a = a + b
a -= b # a = a - b
a *= b # a = a * b
a /= b # a = a / b
a %= b # a = a % b


#string1 = 1 + "String"     - Strings are not numbers, thus cannot be used in calculation
string2 = 2 * "String"
#string3 = 3 - "String"
#string4 = 4 / "String"
result = 2 * int("5") # casting then calculate
print(result)

# boolean variables, truth or false
boolean1 = True # True = 1, False = 0 
boolean2 = not boolean1

# and
boolean3 = True and True
boolean4 = True and False
boolean5 = False and False

# or
boolean6 = True or True
boolean7 = True or False
boolean8 = False or False