import sys
import os
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

os.system('clear')
print("")
playerchoice = input("Enter....\n1. For Rock\n2. For Paper\n3. Scissors\n\nEnter your choice : ")

playerchoice = int(playerchoice)

if playerchoice < 1 or playerchoice > 3:
    sys.exit("You must enter number between 1 and 3!")

computer_choice = int(random.choice("231"))

print("\nYou chose '",str(RPS(playerchoice)).replace('RPS.',''),"'")
print("Bot chose '",str(RPS(computer_choice)).replace('RPS.',''),"'")

print("")
if playerchoice == 1 and computer_choice == 3:
    print("🥳 You win!")
elif playerchoice == 2 and computer_choice == 1:
    print("🥳 You win!")
elif playerchoice == 3 and computer_choice == 2:
    print("🥳 You win!")
elif playerchoice == computer_choice:
    print("😲 It's  a Tie!")
else:
    print("🤖 Wins!")
print("\n")