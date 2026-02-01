
# game={
#     1:"r",2:"p",3:SCISSORS
# }
# winnerCombination={
#     "rr":"draw","pp":"draw","ss":"draw","rp":"p","rs":"r","ps":"s","pr":"p","sr":"r","sp":"s"
# }

# while(True):
#     guessNumber=random.randint(1,3)
#     computGuess=game[guessNumber]
#     userInput=input("rock paper or scissors,r,p,s? ").lower()
#     if(userInput == "r" or userInput == "p" or userInput == "s"):
#         print(f"You choose {userInput}")
#         print(f"computer choose: {computGuess}")
#         combine=computGuess+userInput
#         winner=winnerCombination[combine]
#         if(winner==userInput):
#             print("You Win")

#         elif(winner=="draw"):
#             print("game is draw")
#         else:
#             print("You Loose")
#         coinuation=input("Do you want to coninue (y,n)? ").lower()
#         if(coinuation=="n"):
#             break

#     else:
#         print("enter valid input")
# print("Tanks have a nice day!")

# # print(game[guessNumber])
# # temp="A"
# # if temp !="A":
# #     print(temp)
# # print("test")
import random

ROCK="r"
PAPER="p"
SCISSORS="s"
emojis = {ROCK: "🪨", PAPER: "📃", SCISSORS: "✄"}
user_choices = tuple(emojis.keys())
# user_choices = (ROCK, PAPER, SCISSORS)

def user_choice_function():
    while True:
        userInput = input("rock paper or scissors,r,p,s? ").lower()
        if userInput  in user_choices:
            return userInput
        else:
            print("enter valid input")
            
def displayChoices(userInput,computer_choice):
    print(f"computer choice:{emojis[computer_choice]}")
    print(f"userChoice {emojis[userInput]}")  
    
def decideOutcome(userInput,computer_choice):
    if (userInput == computer_choice):
        return("draw")
    elif ((userInput == PAPER and computer_choice == ROCK) or (userInput == ROCK and computer_choice == SCISSORS) or (userInput == SCISSORS and computer_choice == PAPER)):
        return("user wins")
    else:
        return("You Loose")
    
def playGame():         
    while (True):
        userInput = user_choice_function()
        
        computer_choice = random.choice(user_choices)
        
        displayChoices(userInput,computer_choice)
        
        print(decideOutcome(userInput,computer_choice))
        
        coinuation=input("Do you want to coninue (y,n)? ").lower()
        if(coinuation=="n"):
            break
        else:
            print("enter the valid input")

playGame()