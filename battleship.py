import RPi.GPIO as GPIO
import random

TERRITORY = [
            [[4, 17], [23, 18], [21, 20]], 
            [[27, 22], [15, 14], [16, 12]], 
            [[5, 6], [19, 13], [25, 24]]
            ]

#LED goes red and then green.
EXPANSION1 = [
            [[0,0], [0,0], [0,0]],
            [[0,0], [0,0], [0,0]],
            [[0,0], [0,0], [0,0]]               
        ]

EXPANSION2 = [
            [[0,0], [0,0], [0,0]],
            [[0,0], [0,0], [0,0]],
            [[0,0], [0,0], [0,0]]               
        ]

def printBoard(ledPins, playerBoard):
    for yAxis in range(3):
        for xAxis in range(3):
            #Pull pin numbers
            redLed = ledPins[yAxis][xAxis][0]
            greenLed = ledPins[yAxis][xAxis][1]
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(redLed, GPIO.OUT, initial=0)
            GPIO.setup(greenLed, GPIO.OUT, initial=0)
            #Make led go high or low
            GPIO.output(redLed, playerBoard[yAxis][xAxis][0])
            GPIO.output(greenLed, playerBoard[yAxis][xAxis][1])



def convertLetterNum(letter):
    if letter == "a" or letter == "A":
        return 0
    elif letter == "b" or letter == "B":
        return 1
    else:
        return 2

def matrix():


    print()

#ship placement
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

                    EXPANSION1(prismatic)
                    EXPANSION1[light]
                    EXPANSION1[dark]

                else:

                    EXPANSION2.append(prismatic)
                    EXPANSION2.append(light)
                    EXPANSION2.append(dark)

#running the game loop
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

def atk(board):
    rbd = True

    while rbd == True:
        userShot = input("Select your target coordinates (Ex. A1): ").strip()

        try:
            userShotStr = userShot[0].lower()
            if userShotStr == "a" or userShotStr == "b" or userShotStr == "c":
                userShotInt = int(userShot[1])
                if userShotInt >= 1 and userShotInt <= 3:
                    shipCordX = userShotStr
                    shipCordY = userShotInt - 1
                    
                    shipCordX = convertLetterNum(shipCordX)
                
                    ledList = board[shipCordX][shipCordY]
                    if (ledList[0] == 1 and ledList[1] == 1) or (ledList[0] == 1 and ledList[1] == 0):
                        raise ZeroDivisionError
                    elif (ledList[0] == 0 and ledList[1] == 0): 
                        print("You have missed the target.")
                    elif ledList[0] == 0 and ledList[1] == 1:
                        print("You have hit a ship!")

        except ZeroDivisionError:
            print("You have entered in a location that has already been hit.")
        except:
            print("You have entered in invalid coordinates please try again.")


# Main function

def main():

    matrix()
    player1 = input("What is player 1's name: ")
    redefinition(player1)
    player2 = input("What is player 2's name: ")
    redefinition(player2)
    print("First moves goes to the winner of a coin toss. Player 1 & 2 are heads and tails respectively.")
    player, = coin_toss()
    # Split turns into player 1 and player 2 turns
    


    




main()
