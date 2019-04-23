print("Please enter 5 integers on the following 5 lines:")
lst = [] # create an array or list
lst.append(input()) # add a user input integer into the back
lst.append(input())
lst.append(input())
lst.append(input())
lst.append(input())

# ways to print out an array
print(lst, end = "\n") 
print(*lst, sep = ", ")
