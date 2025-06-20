import RPi.GPIO as GPIO
import random
import time
import os
from colorama import Fore, Style

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

EXPANSION1EnemyBoard = [
                        [[0,0], [0,0], [0,0]],
                        [[0,0], [0,0], [0,0]],
                        [[0,0], [0,0], [0,0]]               
                        ]

EXPANSION2EnemyBoard = [
                        [[0,0], [0,0], [0,0]],
                        [[0,0], [0,0], [0,0]],
                        [[0,0], [0,0], [0,0]]               
                        ]

buzzerPin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT, initial=0)


reinhardOne = []
reinhardTwo = []

cecilusOne = []
cecilusTwo = []

reinhardSunk = 0
cecilusSunk = 0

def wait():
    for i in range(3, 0, -1):
        print("Next turn in ", i)
        time.sleep(1)

def printBoard(ledPins, playerBoard):
    for yAxis in range(3):
        for xAxis in range(3):
            #Pull pin numbers
            redLed = ledPins[yAxis][xAxis][0]
            greenLed = ledPins[yAxis][xAxis][1]
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

#ship placement
def redefinition(player, id):

    print(f"{player}, define your board. You have one 1x1 and one 2x1 ship.")
    # While loop in case of improper inputs
    while True:
        prismatic = input("Place your 1x1 ship (Ex A0): ")
        light = input("Place your first 2x1 ship coordinate (Ex A1): ")
        dark = input("Place your second 2x1 ship coordinate (Ex A2): ")

        if light == prismatic or dark == prismatic or dark == light:

            print("You can't stack ships. Try again.")

        else:

            # Takes user inputs and runs it into function to check if input format & values are correct

            fate = condCheck(prismatic)

            traveler = condCheck(light)
            
            witness = condCheck(dark)

            if traveler == 0 or witness == 0 or fate == 0:

                print("You've input incorrect coordinates. Try again.")
                continue
        
            if traveler == .5:
                
                # 1A --> A1
                formatA = light[1]
                formatB = light[0]
                triumph = formatA + formatB
                light = triumph.strip()
                
            if witness == .5:

                # 1A --> A1
                formatA = dark[1]
                formatB = dark[0]
                nightfall = formatA + formatB
                dark = nightfall.strip()

            if fate == .5:

                # 1A --> A1
                formatA = prismatic[1]
                formatB = prismatic[0]
                excision = formatA + formatB
                prismatic = excision.strip()
            
            if int(light[1]) == 0 and int(dark[1]) == 2 or int(light[1]) == 2 and int(dark[1]) == 0:

                print("Your coordinates list your 2x1 ship as 2 separate entities, which isn't allowed nor possible. Try again.")
                continue

            elif light[0] == "A" and dark[0] == "C" or light[0] == "C" and dark[0] == "A":

                print("Your coordinates list your 2x1 ship as 2 separate entities, which isn't allowed nor possible. Try again.")
                continue
            
            else:

                if id == "ciel":

                    huma = convertLetterNum(prismatic[0])
                    EXPANSION1[huma][int(prismatic[1])][1] = 1

                    jiwald = convertLetterNum(light[0])
                    EXPANSION1[jiwald][int(light[1])][1] = 1

                    shamak = convertLetterNum(dark[0])
                    EXPANSION1[shamak][int(dark[1])][1] = 1

                    reinhard1 = [huma, int(prismatic[1])]
                    reinhardOne.append(reinhard1)

                    reinhard2 = [jiwald, int(light[1])]
                    reinhardTwo.append(reinhard2)

                    reinhard3 = [shamak, int(dark[1])]
                    reinhardTwo.append(reinhard3)
                    
                    break

                else:

                    huma = convertLetterNum(prismatic[0])
                    EXPANSION2[huma][int(prismatic[1])][1] = 1

                    jiwald = convertLetterNum(light[0])
                    EXPANSION2[jiwald][int(light[1])][1] = 1

                    shamak = convertLetterNum(dark[0])
                    EXPANSION2[shamak][int(dark[1])][1] = 1

                    cecilus1 = [huma, int(prismatic[1])]
                    cecilusOne.append(cecilus1)

                    cecilus2 = [jiwald, int(light[1])]
                    cecilusTwo.append(cecilus2)

                    cecilus3 = [shamak, int(dark[1])]
                    cecilusTwo.append(cecilus3)

                    break

#running the game loop
def pleiades(player, player1, player2):

    while True:
        if player == "Player 1":
            playerID = "ciel"
            printBoard(TERRITORY, EXPANSION2EnemyBoard)
            atk(EXPANSION2, EXPANSION2EnemyBoard)
            isSunk(playerID,cecilusOne, cecilusTwo, EXPANSION2EnemyBoard, player1, player2)
            printBoard(TERRITORY, EXPANSION2EnemyBoard)

            wait()
            print("Player 2's turn:")
            playerID = "tempest"
            printBoard(TERRITORY, EXPANSION1EnemyBoard)
            atk(EXPANSION1, EXPANSION1EnemyBoard)
            isSunk(playerID,reinhardOne, reinhardTwo, EXPANSION1EnemyBoard, player1, player2)
            printBoard(TERRITORY, EXPANSION1EnemyBoard)

            wait()
            print("Player 1's turn")

        else:
            playerID = "tempest"
            printBoard(TERRITORY, EXPANSION1EnemyBoard)
            atk(EXPANSION1, EXPANSION1EnemyBoard)
            isSunk(playerID,reinhardOne, reinhardTwo, EXPANSION1EnemyBoard, player1, player2)
            printBoard(TERRITORY, EXPANSION1EnemyBoard)

            wait()
            print("Player 1's turn:")
            playerID = "ciel"
            printBoard(TERRITORY, EXPANSION2EnemyBoard)
            atk(EXPANSION2, EXPANSION2EnemyBoard)
            isSunk(playerID,cecilusOne, cecilusTwo, EXPANSION2EnemyBoard, player1, player2)
            printBoard(TERRITORY, EXPANSION2EnemyBoard)

            wait()
            print("Player 2's turn")

# checks the players' inputs for their ship locations to make sure their valid
def condCheck(paracausal):
    
    consciousness = 0
    Guardian = .5
    diety = 1
    
    try:

        # If the format is correct (LetterNumber) & values are correct, returns correct
        if paracausal[0].isalpha() == True and paracausal[1].isdigit() == True:

            # If they are within range (A-C) or (0-2)
            if paracausal[0].upper() != "A" and paracausal[0].upper() != "B" and paracausal[0].upper() != "C":

                return consciousness

            elif int(paracausal[1]) != 0 and int(paracausal[1]) != 1 and int(paracausal[1]) != 2:

                return consciousness

            else:

                return diety

        # IF the format is wrong but values are correct, returns partially correct
        if paracausal[0].isdigit() == True and paracausal[1].isalpha() == True:

            if int(paracausal[0]) != 0 and int(paracausal[0]) != 1 and int(paracausal[0]) != 2:

                return consciousness

            elif paracausal[1].upper() != "A" and paracausal[1].upper() != "B" and paracausal[1].upper() != "C":

                return consciousness

            else:

                return Guardian
        else:

            # If the values are wrong, returns incorrect
            return consciousness
        
    except ValueError:
        print()

# randomly decides who starts if the player so chooses
def coin_toss():

    result = random.randint(0,1)
    if result == 0:

        print("Player 1's move.")
        return "Player 1"
    
    else:

        print("Player 2's move.")
        return "Player 2"

# determines both whether or not a ship has sunk, as well as whether or not someone has won (upon sinking both ships)
def isSunk(id, matrix1, matrix2, parameter, playerName, playerName2):
    global cecilusSunk, reinhardSunk
    if id == "ciel":
        name = playerName
    else:
        name = playerName2
    
    for item in matrix1:
        xCoord = item[0]
        yCoord = item[1]

        if parameter[xCoord][yCoord][0] == 1 and parameter[xCoord][yCoord][1] == 1:
            print(f"{name} has sunk the 1x1 ship.")
            GPIO.output(buzzerPin , 1)
            time.sleep(0.5)
            GPIO.output(buzzerPin , 0)
            parameter[xCoord][yCoord][0] = 1
            parameter[xCoord][yCoord][1] = 0
            if id == "ciel":
                reinhardSunk += 1
            else:
                cecilusSunk += 1
            del matrix1
            break
    hitMark = 0
    for item in matrix2:
        xCoord = item[0]
        yCoord = item[1]

        if parameter[xCoord][yCoord][0] == 1 and parameter[xCoord][yCoord][1] == 1:
            hitMark += 1

            if hitMark == 2:
                print(f"{name} has sunk the 2x1 ship!")
                for item2 in matrix2:
                    xCoord2 = item2[0]
                    yCoord2 = item2[1]
                    parameter[xCoord2][yCoord2][0] =  1
                    parameter[xCoord2][yCoord2][1] =  0
                GPIO.output(buzzerPin , 1)
                time.sleep(0.5)
                GPIO.output(buzzerPin , 0)
                if id == "ciel":
                    reinhardSunk += 1
                else:
                    cecilusSunk += 1
                del matrix2
    if cecilusSunk == 2 or reinhardSunk == 2:
        printBoard(TERRITORY, parameter)
        print(f"{name} has sunk both of the ships. They have won!")
        time.sleep(3)
        GPIO.cleanup()
        quit()


# Combat functions
def atk(board, seenBoard):
    rbd = True


    while rbd == True:
        userShot = input("Select your target coordinates (Ex. A0): ").strip()


        try:
            userShotStr = userShot[0].lower()
            if userShotStr == "a" or userShotStr == "b" or userShotStr == "c":
                userShotInt = int(userShot[1])
                if userShotInt >= 0 and userShotInt <= 2:
                    shipCordX = userShotStr
                    shipCordY = userShotInt
                   
                    shipCordX = convertLetterNum(shipCordX)
               
                    ledList = board[shipCordX][shipCordY]

                    #check if there are already shots at the location
                    if (ledList[0] == 1 and ledList[1] == 1) or (ledList[0] == 1 and ledList[1] == 0):
                        raise ZeroDivisionError
                    elif (ledList[0] == 0 and ledList[1] == 0):
                        print("You have missed the target.")
                        board[shipCordX][shipCordY][0] = 0
                        board[shipCordX][shipCordY][1] = 1
                        seenBoard[shipCordX][shipCordY][0] = 0
                        seenBoard[shipCordX][shipCordY][1] = 1
                    elif ledList[0] == 0 and ledList[1] == 1:
                        print("You have hit a ship!")
                        board[shipCordX][shipCordY][0] = 1
                        board[shipCordX][shipCordY][1] = 1
                        seenBoard[shipCordX][shipCordY][0] = 1
                        seenBoard[shipCordX][shipCordY][1] = 1
                    rbd = False
            else:
                raise


        except ZeroDivisionError:
            print("You have entered in a location that has already been hit.")
        except:
            print("You have entered in invalid coordinates. Please try again.")



# Main function

def main():

    print(f"""Player one inputs their name and will subsequently place their ships. 
        Following placement, you receive a 3-second window to view where you placed your ships. 
        Player 2 ideally looks away at this time so as to avoid gaining an unfair advantage. 
        The same thing applies while player 2 places their ships. 
        'A' corresponds to the first (top) row, followed by 'B' (center) and continuing on with 'C' being the last (bottom) row. 
        '0' corresponds to the first (left) column, followed by '1' (center) and finishing with 2 being the last (right) column. 
        During battle, you will see LED's begin to glow. {Fore.GREEN}Green{Fore.RESET} signifies a miss, {Fore.LIGHTRED_EX}Orange{Fore.RESET} signifies a hit, and {Fore.RED}Red{Fore.RESET} signifies a sunk ship. 
        Good luck!\n""")

    player1 = input("Enter player 1's name: ")
    id1 = "ciel"
    redefinition(player1, id1)
    printBoard(TERRITORY, EXPANSION1)
    wait()
    os.system('clear')
    printBoard(TERRITORY, EXPANSION1EnemyBoard)

    player2 = input("Enter player 2's name: ")
    id2 = "tempest"
    redefinition(player2, id2)
    printBoard(TERRITORY, EXPANSION2)
    wait()
    os.system('clear')
    printBoard(TERRITORY, EXPANSION1EnemyBoard)

    # Split turns into player 1 and player 2 turns
    
    while True:

        satella = int(input("How would you like to determine who goes first: Manual selection or leave it to fate? (0 or 1): "))

        if satella == 1:

            print("First moves goes to the winner of a coin toss. Player 1 & 2 are heads and tails respectively.")
            player = coin_toss()
            break

        elif satella == 0:

            player = int(input("Enter 1 for player 1 and 2 for player 2: "))

            if player == 1:

                player = "Player 1"
                print(f"{player}'s turn.")

                break

            elif player == 2:

                player = "Player 2"
                print(f"{player}'s turn.")

                break

            else:

                print("The options in a 2 player game are 1 and 2. Please try again.")
                continue
        
        else:

            print("Either you pick or the computer picks for you. Please try again.")
            continue

    pleiades(player, player1, player2)

    



main()
