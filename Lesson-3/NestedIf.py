coin = input().lower() # head or tail
card = input().lower() # red or black

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