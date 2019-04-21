import random
array = []
array = [random.randint(1, 100) for i in range (10)]
print(*array, sep = ", ")

# acssending
print("\nSort Ascending:")
array.sort()
sorted(array)
print(*array, sep = ", ")

# descending
print("\nSort Descending:")
array.sort(reverse = True)
sorted(array, reverse = True)
print(*array, sep = ", ")

print("\nAdd elements:")
array.append("Unique")
array.insert(5, "Also Unique")
array[0] = "Unique"
print(*array, sep = ", ")

print("\nRemove elements:")
array.remove("Unique")
print(*array, sep = ", ")
array.pop(-1)
print(*array, sep = ", ")
del array[4]
print(*array, sep = ", ")
