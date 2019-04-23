print("Hello World!") # Hello World!

print(input()) # Immediate output out the input

print("1, ") # Default print with newline
print("2")

print("1,", end=" ") # motified print, multiple information on one line
print("2")

print("1,", end="\n") # motified print, but the same effect as default print
print("2")

print("%d %.2f %s" % (10, 50.0, "String")) # formated print, print Integers, rounded decimals, and string