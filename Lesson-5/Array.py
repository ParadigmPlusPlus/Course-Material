import random
array = []
array = [random.randint(1, 101) for i in range (10)]
print(array)

#for i in range (1, 11, 1):
for i in range(0, 10, 1):
    print("index: %d, value: %d" % (i, array[i]), end = "\n")
