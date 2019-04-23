import random
# pass by value
def p(message):
	message = "Hey"
	print(message)


def findGD (a): # define the greatest difference between 2 adjecent elements
    greatest = 0
    prev = a[0]
    for v in a:
        greatest = max(greatest, abs(prev - v))
        prev = v
    return greatest


# pass by reference
def makeSum(a): # turn the array into an array of sum to that point
    a.insert(0, 0)
    for i in range (1, len(a), 1):
        a[i] += a[i - 1]


message = "X mark the spot"
p(message) # a faster print method
print()

a = [random.randint(1, 100) for i in range (10)]
print(*a, sep = ", ")
print("Greatest difference between 2 adjacent element in an unsorted list is: %d" % findGD(a)) # first time using the method
a.sort()
print(*a, sep = ", ")
print("Greatest difference between 2 adjacent element in a sorted list is: %d" % findGD(a)) # second time using the method
print()

makeSum(a)
print(*a, sep = ", ") # the array is altered, even though it wasn't in the same method
