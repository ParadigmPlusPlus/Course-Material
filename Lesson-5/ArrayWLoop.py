import random
array = [random.randint(1, 100) for i in range (10)] 
array.sort()

# Wrong or inefficient way of looping through array
# for i in range (1, 10 + 1, 1):
# for i in range (0, 9 + 1, 1):
for i in range (10):
    print(array[i], end = ", ")
print()

# find sum of the array
sum = 0
for v in array: # utilize "v in V"
    print("%d + %d = " % (sum, v), end = "")
    sum += v # add each value into the sum
    print(sum)
print("The sum is: %d" % sum)

# find greatest even number in an array of number
found = False
greatest = 0
for v in array:
    if v % 2 == 0: # if the number is even
        if not found: # if no even have been found
            greatest = v # the number is thus greatest
            found = True
        else:
            greatest = max(greatest, v) # compare the new even number with previously greatest even number
if found:
    print("The greatest EVEN number in the array is: %d" % greatest)
else:
    print("No EVEN number was found")
