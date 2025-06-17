import random

TERRITORY = [[4, 17], [23, 18], [21, 20], 
             [27, 22], [15, 14], [16, 12], 
             [5, 6], [19, 13], [25, 24]]

EXPANSION = []

def matrix():

    print()


def redefinition(player):

    print(f"{player}, define your board. You have one 1x1 and one 2x1 ship.")
    while True:
        prismatic = input("Place your 1x1 ship (Ex 1A or A1): ")
        light = input("Place your first 2x1 ship coordinate (Ex A1 or 1A): ")
        dark = input("Place your second 2x1 ship coordinate (Ex B1 or 2A)")

        if light == prismatic or dark == prismatic:

            print("Everybody knows you can't stack ships. Try again.")

        else:

            if light.split[0] == str and int(light.split[1]) == int:

                if light.split[0].upper() != "A" or light.split[0].upper() != "B" or light.split[0].upper() != "C":
                    print("This is as far as you go. Please input coordinates within bounds.")
                elif int(light.split[1]) != 1 or 2 or 3:
                    print("This is as far as you go. Please input coordinates within bounds.")

            if int(light.split[0]) == int and light.split[1] == str:

                if int(light.split[0]) != 1 or int(light.split[0]) != 2 or int(light.split[0]) != 3:
                    print()
                elif light.split[1].upper() != "A" or light.split[1].upper() != "B" or light.split[1].upper() != "C":
                    print()


def game_start():

    print()

def coin_toss():

    result = random.randint(0,1)
    if result == 0:
        return "Player 1"
    else:
        return "Player 2"

# Combat functions

def atk():

    reg = input("Select your target coordinates (Ex. 1A or A1): ")
    rbd = True
    while rbd == True:
        if reg.split[0] == str and reg.split[1] == int:
            # If they input A1 or something similar
            xCoor = reg.split[0]
            yCoor = reg.split[1]
            format = (xCoor,yCoor)
            # Returns (Letter, Number)
            rbd = False
        elif reg.split[0] == int and reg.split[1] == str:
            # If they input 1A or something similar
            xCoor = reg.split[1]
            yCoor = reg.split[0]
            format = (yCoor,xCoor)
            # Returns (Letter,Number)
            rbd = False
        else:
            print("You've input improper coordinates. Please retry.")
            rbd = True
    return format

def hitreg(decision, player):

    if player == "Player 1":
        
        if decision.split[0] == 
    else:

        print()

def miss():

    print()

# Main function

def main():

    matrix()
    player1 = input("What is player 1's name: ")
    redefinition(player1)
    player2 = input("What is player 2's name: ")
    redefinition(player2)
    print("First moves goes to the winner of a coin toss. Player 1 & 2 are heads and tails respectively.")
    player = coin_toss()
    # Split turns into player 1 and player 2 turns
    decision = atk()
    hitreg(decision, player)

    decision = atk()
    hitreg(decision, player)


    




main()