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
import random

game= [rock, paper, scissors]
pers_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if pers_choice > 2 or pers_choice < 0:
    print("You lose")
else:
    print(game[pers_choice])

    game_rand = random.randint(0, 2)
    print(f"Computer choice:\n{game[game_rand]}")

    if (pers_choice == 0 and game_rand == 1) or (pers_choice == 1 and game_rand == 2) or (pers_choice == 2 and game_rand == 0) :
        print("You lose.")
    elif (pers_choice == 0 and game_rand == 2) or (pers_choice == 1 and game_rand == 0) or (pers_choice == 2 and game_rand == 1):
        print("You win!")
    else:
        print("Draw")







