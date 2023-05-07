import random

logo = """
  _   _                 _                  _____                    _                _____                      
 | \ | |               | |                / ____|                  (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___ ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ | '__| | | |_ | | | |/ _ / __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __| |    | |__| | |_| |  __\__ \__ | | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___|___|___|_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                             __/ |                              
                                                                            |___/                               
"""



def easy(answer, number, lives):
    while answer != number and lives > 1:
        if answer > number:
            lives -= 1
            print(f"Too high.\n Guess again\n You have {lives} attempts remaining to guess the number")
            answer = int(input("Make a guess: "))

        elif answer < number:
            lives -= 1
            print(f"Too low.\n Guess again\n You have {lives} attempts remaining to guess the number")
            answer = int(input("Make a guess: "))
    if answer == number:
        print(f"You got it! The answer was {number}")
    else:
        print("You lose. Try more!")


def hard(answer, number, lives):
    while answer != number and lives > 1:
        if answer > number:
            lives -= 1
            print(f"Too high.\n Guess again\n You have {lives} attempts remaining to guess the number")
            answer = int(input("Make a guess: "))

        elif answer < number:
            lives -= 1
            print(f"Too low.\n Guess again\n You have {lives} attempts remaining to guess the number")
            answer = int(input("Make a guess: "))
    if answer == number:
        print(f"You got it! The answer was {number}")
    else:
        print("You lose. Try more!")


def number_guessing():
    print(logo)
    print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    print(f"Psssst, the right answer is {number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        lives = 10
        print("You have 10 attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))
        easy(answer, number, lives)
    elif difficulty == 'hard':
        lives = 5
        print("You have 5 attempts remaining to guess the number.")
        answer = int(input("Make a guess: "))
        hard(answer, number, lives)


number_guessing()





