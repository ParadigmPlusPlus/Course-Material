print("Enter the coin result, or enter END to end")
coin = input().lower() 
while coin != "end":
    print("Enter card colour")
    card = input().lower()

    # clear leveling
    if coin == "head":
        if card == "red":
            print("You won")
        elif card != "red":
            print("Lost")
        else:
            print("HOW?")
    elif coin == "tail":
        if card == "black":
            print("You won")
        elif card != "black":
            print("Lost")
        else:
            print("HOW?")
    else:
        print("HOW?")

    print("Enter the coin result, or enter END to end")
    coin = input().lower() 