import random

rock = ("rock")
paper = ("paper")
scissors = ("scissors")

options = [rock, paper, scissors]
Pscore = 0
Mscore = 0

def Game():
        global Pscore
        global Mscore

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
                print(" ")
                Game()

for x in range(3):
        print(" ")
        Game()


print("Player score = " + str(Pscore))
print("Computer score = " + str(Mscore))