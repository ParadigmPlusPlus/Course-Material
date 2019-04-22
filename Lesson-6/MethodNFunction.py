import random
def findGD (a):
    great = 0
    prev = a[0]
    for v in a:
        great = max(great, abs(prev - v))
        prev = v
    return great


def makeSum(a):
    a.insert(0, 0)
    for i in range (1, len(a), 1):
        a[i] += a[i - 1]


a = [random.randint(1, 100) for i in range (10)]
print(*a, sep = ", ")
print("Greatest difference between 2 adjacent element in an unsorted list is: %d" % findGD(a)) # first time using the method
a.sort()
print(*a, sep = ", ")
print("Greatest difference between 2 adjacent element in a sorted list is: %d" % findGD(a)) # second time using the method

makeSum(a)
print(*a, sep = ", ")
