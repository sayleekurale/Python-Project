import random

options = ("Rock", "Paper", "Scissors")


running=True

while running:
    players = None
    computer = random.choice(options)

    while players not in options:
        players = input("Enter a choice (Rock, Paper, Scissors) : ")

    print(f"players : {players}")
    print(f"computer : {computer}")

    if players == computer:
        print("Its a tie!!!")
    elif players == "Rock" and computer == "Scissors":
        print("Congrats you Win!!")
    elif players == "Paper" and computer == "Rock":
        print("Congrats you Win!!")
    elif players == "Scissors" and computer == "Paper":
        print("Congrats you Win!!")
    else:
        print("offo you lose!")
    play_again = input("Play Again ?? (Y/N): ").lower()
    if not play_again =="y/Y":
        running=False


print("Thanks For Playing")