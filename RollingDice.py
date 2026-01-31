import random
while(True):
    dice=input("roll the dice (y/n): ").lower()
    if(dice=="y"):
        num1=random.randint(1,6)
        num2=random.randint(1,6)
        print(f"({num1},{num2})")
    elif(dice=="n"):
        print("Thanks for Playing")
        break
    else:
        print("Please enter the valid input")
        continue