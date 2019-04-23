import random
def printArray(a):
    print(*a, sep = ", ", end = "\n\n")


array = []
array = [random.randint(1, 100) for i in range (10)]
print(*array, sep = ", ")

# acssending sorting
array.sort()
array = sorted(array)
printArray(array)


# descending sorting
array.sort(reverse = True)
array = sorted(array, reverse = True)
printArray(array)

# add and replace elements
array.append("Unique") # add to back
array.insert(5, "Also Unique") # add to index 5
array[0] = "Unique"
printArray(array)

# remove elements
del array[5] # remove index 4
printArray(array)
array.remove("Unique") # remove first occurance
printArray(array)
array.pop(-1) # remove last index
printArray(array)


