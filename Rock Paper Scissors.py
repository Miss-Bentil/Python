import random

choices = ["rock","paper","scissors"]


def play():
    computer = random.choice(choices)
    player = input("Enter your choice: ").lower()

    if player in choices:
        if player == "rock":
            if computer == "scissors":
                print(f"Yaay you have won !!!. You picked {player} and the computer picked {computer}.")
            elif computer == "paper":
                print(f"Oops you lost this round :( You picked {player} and the computer picked {computer}.")
        elif player == "paper":
            if computer == "rock":
                print(f"Yaay you have won !!! You picked {player} and the computer picked {computer}.")
            elif computer == "scissors":
                print(f"Oops you lost this round :( You picked {player} and the computer picked {computer}.")
        elif player == "scissors":
            if computer == "paper":
                print(f"Yaay you have won !!!You picked {player} and the computer picked {computer}.")
            elif computer == "rock":
                print(f"Oops you lost this round :( You picked {player} and the computer picked {computer}.")
        else:
            if player == computer:
                print(f"Its a tie. You picked {player} and the computer picked{computer}")
    else:
        print("The choice you have made is not correct. Try again.")

play()

while True:
    playAgain = input("Would you like to play again? Yes or No? : ").lower()
    if "no" in playAgain:
        print("Goodbye. Have yourself a lovely day!")
        break
    else:
        if "yes" in playAgain:
            play()












