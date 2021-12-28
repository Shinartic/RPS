import random

rock = ("rock")
paper = ("paper")
scissors = ("scissors")

options = [rock, paper, scissors]
Pscore = 0
Mscore = 0
games_amount = 3

def Game():
        global Pscore
        global Mscore
        global games_amount

        userinput = input("rock, paper, scissors shoot!: ")

        robotinput = random.choice(options)

        print("The robot chose: " + robotinput)

        if userinput == ("rock") and robotinput == "rock":
                print("Tie")
        elif userinput == ("rock") and robotinput == "paper":
                print("You lost")
                Mscore += 1
        elif userinput == ("rock") and robotinput == "scissors":
                print("You won")
                Pscore += 1
        elif userinput == ("paper") and robotinput == "rock":
                print("You won")
                Pscore += 1
        elif userinput == ("paper") and robotinput == "paper":
                print("Tie")
        elif userinput == ("paper") and robotinput == "scissors":
                print("You lost")
                Mscore += 1
        elif userinput == ("scissors") and robotinput == "rock":
                print("You lost")
                Mscore += 1
        elif userinput == ("scissors") and robotinput == "paper":
                print("You won")
                Pscore += 1
        elif userinput == ("scissors") and robotinput == "scissors":
                print("Tie")
        else:
                print("Invalid input, try again")
                games_amount += 1

        print("  ")

for x in range(games_amount):
        Game()


print("Player score = " + str(Pscore))
print("Computer score = " + str(Mscore))