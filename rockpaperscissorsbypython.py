import random 
import os
import re
while(1<2):
    
    #define game
    print("\n")
    print("Rock. Paper. Scissors.....Shoot!")

    user_choice=input("Choose your weapon [R]ock,[P]aper,[S]cissors,[E]xit")

    if (not re.match("[SsRrPpEe]",user_choice)) or (len(user_choice)!=1):
        print("Please choose a letter: ")
        print("R]ock,[P]aper,[S]cissors,or [E]xit")
        continue
    if (user_choice=="E"or user_choice=="e"):
        print("Exiting Game....")
        break
    choices=["R","P","S"]

    opponent_choice=random.choice(choices)
    
    print("I chose: "+opponent_choice)

    if opponent_choice==str.upper(user_choice):
        print("Tie!")
        continue
    elif opponent_choice=="R" and user_choice.upper()=="S":
        print("Rock beats scissors,I win")
        continue
    elif opponent_choice=="S" and user_choice.upper()=="P":
        print("Scissors  cuts Ppaer,I win")
        continue
    elif opponent_choice=="P" and user_choice.upper()=="R":
        print("paper hides rock,I win")
        continue
    else:
        print("You won!!")
    