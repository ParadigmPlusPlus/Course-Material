print("If you flip HEAD and got RED, or flip TAIL and got BLACK, you win")
print("Enter the coin result, or enter END to end")
coin = input().lower() # head or tail

while coin != "end" :
    print("Enter card colour")
    card = input().lower()# red or black

    # not so much logic, long complicated if statement
    if coin == "head" and card == "red":
        print("Yoou won!")
    elif coin == "head" and card != "red":
        print("Lost")
    elif coin == "tail" and card == "black":
        print("You won!")
    elif coin == "tail" and card != "black":
        print("Lost")
    else:
        print("HOW?")

    print("Enter the coin result, or enter END to end")
    coin = input().lower() 