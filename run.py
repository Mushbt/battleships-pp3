# Player game board
P_BOARD = [[" "] * 8 for i in range(8)]
# Computer game board
C_BOARD = [[" "] * 8 for i in range(8)]

SHIP_LENGTHS = [2, 3, 3, 4, 5]

board_coordinates = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

def intro():
    print("Welcome to battleships!\n")
    print("Battleships is a strategy type guessing game\n")
    print("It is played on a ruled grid (In this case 8x8)\n")
    print("You and the computer will have 5 ships each with different sizes\n")
    print("The location of the ships will be concealed from each other\n")
    print("You will take turns calling coordinates trying to sink eachothers ships\n")
    print("The objective of the game is to try and sink all the computers ships\n")
    print("When this has been achieved bu either you or the computer, the game will be over")

    print("You will have the following ships in your fleet:\n")
    print("DESTROYER - 2 BOARD POSITIONS")
    print("SUBMARINE - 3 BOARD POSITIONS")
    print("CRUISER - 3 BOARD POSITIONS")
    print("BATTLESHIP -  4 BOARD POSITIONS")
    print("CARRIER - 5 BOARD POSITIONS")

    print("The following is the game legend:")
    print("@ - SHIP")
    print("O - MISSED TARGET")
    print("X - HIT TARGET")