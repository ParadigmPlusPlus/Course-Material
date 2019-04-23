# simple while loop achieveing same effect as the eariler for loop
counter = 0 
while counter != 10: # a loop that runs 10 times
    print(counter, end="")
    counter += 1 # increment to meet the exit condition
print()

counter = 10
while counter != 0:
    print(counter, end="")
    counter -= 1 # reduction instead of increment

user = input().lower()
while user != "your name": # while loop doesn't have to be only adding
    print("Please enter your name:")
    user = input().lower()