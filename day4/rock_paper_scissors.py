import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices = [rock, paper, scissors]
players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

computers_choice = random.randint(0, 2)

#If the player chose any other number than 0, 1 or 2
if players_choice >= 3 or players_choice < 0:
    print("Invalid number")

#if the player chose rock
if players_choice == 0 and computers_choice == 1 :
    print(rock)
    print(f"Computer chose : \n{paper}")
    print("You lose")

if players_choice == 0 and computers_choice == 2 :
    print(rock)
    print(f"Computer chose : \n{scissors}")
    print("You win")


# If players chose Paper
if players_choice == 1 and computers_choice == 0:
    print(paper)
    print(f"Computer chose : \n{rock}")
    print("You win")

if players_choice == 1 and computers_choice == 2 :
    print(paper)
    print(f"Computer chose : \n{scissors}")
    print("You lose")

# If players chose Scissors
if players_choice == 2 and computers_choice == 0:
    print(scissors)
    print(f"Computer chose : \n{rock}")
    print("You lose")

if players_choice == 2 and computers_choice == 1 :
    print(scissors)
    print(f"Computer chose : \n{paper}")
    print("You win")

#if it's a draw
if players_choice == computers_choice :
    print(choices[players_choice])
    print(f"Computer chose : \n {choices[computers_choice]}")
    print("You draw")
