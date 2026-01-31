import random
computerGuess=random.randint(1,100)
while(True):
    try:
        userInput=int(input("please guess the number from 1 to 100 "))
        if(computerGuess>userInput):
            print("your number is low")
        if(computerGuess<userInput):
            print("your number is High")
        if(userInput==computerGuess):
            print("Right Guess!")
            break
    except ValueError:
        print("please enter the valid number")
    
    
    