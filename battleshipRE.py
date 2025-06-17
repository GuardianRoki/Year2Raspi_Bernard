import random

TERRITORY = [[4, 17], [23, 18], [21, 20], 
             [27, 22], [15, 14], [16, 12], 
             [5, 6], [19, 13], [25, 24]]

EXPANSION1 = []
EXPANSION2 = []

def matrix():


    print()

# Ship creation/placement
def redefinition(player):

    print(f"{player}, define your board. You have one 1x1 and one 2x1 ship.")
    while True:
        prismatic = input("Place your 1x1 ship (Ex 1A or A1): ")
        light = input("Place your first 2x1 ship coordinate (Ex A1 or 1A): ")
        dark = input("Place your second 2x1 ship coordinate (Ex B1 or 2A): ")

        if light == prismatic or dark == prismatic or dark == light:

            print("You can't stack ships. Try again.")

        else:

            traveler = condCheck(light)
            
            witness = condCheck(dark)

            if traveler == 0 or witness == 0:

                print("You've input incorrect coordinates. Try again.")
                continue
        
            if traveler == 0.5:
                
                # 1A --> A1
                formatA = light[1]
                formatB = light[0]
                triumph = formatA + formatB
                light = triumph.strip(" ")
                
            if witness == 0.5:

                # 1A --> A1
                formatA = dark[1]
                formatB = dark[0]
                nightfall = formatA + formatB
                dark = nightfall.strip(" ")
            
            if int(light[1]) == 1 and int(dark[1]) == 3 or int(light[1]) == 3 and int(dark[1]) == 1:

                print("Your coordinates list your 2x1 ship as 2 separate entities, which isn't allowed nor possible. Try again.")
                continue

            elif light[0] == "A" and dark[0] == "C" or light[0] == "C" and dark[0] == "A":

                print("Your coordinates list your 2x1 ship as 2 separate entities, which isn't allowed nor possible. Try again.")
                continue
            
            else:

                if player == "Player 1":

                    EXPANSION1.append(prismatic)
                    EXPANSION1[light]
                    EXPANSION1[dark]

                else:

                    EXPANSION2.append(prismatic)
                    EXPANSION2.append(light)
                    EXPANSION2.append(dark)


def pleiades():

    print()

def game_set():

    print()

def condCheck(paracausal):
    
    consciousness = 0
    Guardian = .5
    diety = 1

    # If the format is correct (LetterNumber) or (NumberLetter)
    if type(paracausal[0]) == type(str) and type(paracausal[1]) == type(int):

        # If they are within range (A-C) or (1-3)
        if paracausal[0].upper() != "A" or paracausal[0].upper() != "B" or paracausal[0].upper() != "C":

            return consciousness

        elif int(paracausal[1]) != 0 or int(paracausal[1]) != 1 or int(paracausal[1]) != 2:

            return consciousness

        else:

            return diety

    elif type(paracausal[0]) == type(int) and type(paracausal[1]) == type(str):

        if int(paracausal[0]) != 0 or int(paracausal[0]) != 1 or int(paracausal[0]) != 2:

            return consciousness

        elif paracausal[1].upper() != "A" or paracausal[1].upper() != "B" or paracausal[1].upper() != "C":

            return consciousness

        else:

            return Guardian
    else:

        return consciousness


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
        if type(reg.split[0]) == type(str) and type(reg.split[1]) == type(int):
            # If they input A1 or something similar
            xCoor = reg.split[0]
            yCoor = reg.split[1]
            format = (xCoor,yCoor)
            # Returns (Letter, Number)
            rbd = False
        elif int(reg.split[0]) == int and reg.split[1] == str:
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

# def hitreg(decision, player):

#     if player == "Player 1":
        
#         if decision.split[0] == 
#     else:

#         print()

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
    # hitreg(decision, player)

    decision = atk()
    # hitreg(decision, player)


    




main()
