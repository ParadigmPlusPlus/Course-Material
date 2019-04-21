import random
array = [random.randint(1, 100) for i in range (10)]
array = sorted(array)
# Wrong or inefficient way of looping through array
# for i in range (1, 10 + 1, 1):
# for i in range (0, 9 + 1, 1):
for i in range (10):
    print(array[i], end = " ")
print()

sum = 0
for v in array: # utilize "v in V"
    print("%d + %d = " % (sum, v), end = "")
    sum += v
    print(sum)
print("The sum is: %d" % sum)

found = False
greatest = 0
for v in array:
    if v % 2 == 0:
        if not found:
            greatest = v
            found = True
        else:
            greatest = max(greatest, v)
if found:
    print("The greatest EVEN number in the array is: %d" % greatest)
else:
    print("No EVEN number was found")
