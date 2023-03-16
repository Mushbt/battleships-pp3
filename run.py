"""
Modules
"""
import random
import sys
import time

# Player game board
P_BOARD = [[" "] * 8 for i in range(8)]
# Computer game board
C_BOARD = [[" "] * 8 for i in range(8)]

# Ship lengths of all ships on board
SHIP_LENGTHS = [2, 3, 3, 4, 5]

# Board coordinates which will allow player to
# guess where the computers ships are located on board
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


def print_fast(ltr):
    """
    Creates a fast typing effect
    """
    for letter in ltr:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def print_slow(ltr):
    """
    Creates a slow typing effect
    """
    for letter in ltr:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


# Game introduction
def intro():
    """
    This is the game introduction. Game logo, and welcome
    message will print which is followed by a question
    of if the player has played this game before
    """
    print_fast("""\
    \u001B[31m
  ____        _   _   _           _     _
 |  _ \      | | | | | |         | |   (_)
 | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___
 |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ |
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                         | |
                                         |_|
\u001b[0m
""")

    print_slow("Welcome to battleships!\n")
    time.sleep(1)
    print(' ')
    print_slow("Have you played battleships before?\n")
    answer = input("Enter Y or N\n").upper()
    print(' ')
    while True:
        if answer == "Y":
            start_game()
        elif answer == "N":
            instructions()
        else:
            print(' ')
            print_slow("Please enter Y or N\n")
            answer = input("").upper()


def instructions():
    """
    Game instructions will print if player
    has not played the game before.
    """
    print_slow("Battleships is a strategy type guessing game\n")
    print_slow("It is played on a ruled grid (In this case 8x8)\n")
    print_slow("You and the computer will have 5 ships each with different \
sizes\n")
    print_slow("The location of the ships will be concealed from each other\n")
    print_slow("You will take turns calling coordinates trying to sink \
eachothers ships\n")
    print_slow("The objective of the game is to try and sink all the \
computers ships\n")
    print_slow("When this has been achieved by either you or the computer, \
the game will be over\n")
    time.sleep(3)
    print(' ')
    # Ships and sizes
    print_slow("You will have the following ships in your fleet:\n")
    print_slow("\u001B[32mDESTROYER \u001B[0m- 2 BOARD POSITIONS\n")
    print_slow("\u001B[33mSUBMARINE \u001B[0m- 3 BOARD POSITIONS\n")
    print_slow("\u001B[34mCRUISER \u001B[0m- 3 BOARD POSITIONS\n")
    print_slow("\u001B[35mBATTLESHIP \u001B[0m- 4 BOARD POSITIONS\n")
    print_slow("\u001B[31mCARRIER \u001B[0m- 5 BOARD POSITIONS\n")
    time.sleep(3)
    print(' ')
    # Game legend
    print_slow("The following is the game legend:\n")
    print_slow("@ - SHIP\n")
    print_slow("O - MISSED TARGET\n")
    print_slow("X - HIT TARGET\n")
    time.sleep(3)
    print(' ')
    start_game()


def print_board(board):
    """
    The print board function prints out the game board
    """
    print('  A B C D E F G H')
    row_num = 1
    for row in board:
        row_str = "%d|%s|" % (row_num, "|".join(row))

        # Hide the ship positions on computers board
        if board is C_BOARD:
            row_str = row_str.replace('@', ' ')

        print(row_str)
        row_num += 1


def print_ship(board):
    """
    The print ship function will automatically print the ships
    on the board for both the player and computer while checking
    the ships fit on the board and check for any overlapping
    """
    for ship_length in SHIP_LENGTHS:
        while True:
            if board == C_BOARD:
                direction, row, column = random.choice(["H", "V"]), \
                    random.randint(0, 7), random.randint(0, 7)
                if ship_fits(ship_length, row, column, direction):
                    if not check_overlap(board, row, column, direction,
                                         ship_length):
                        if direction == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "@"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "@"
                        break
            if board == P_BOARD:
                direction, row, column = random.choice(["H", "V"]), \
                    random.randint(0, 7), random.randint(0, 7)
                if ship_fits(ship_length, row, column, direction):
                    if not check_overlap(board, row, column, direction,
                                         ship_length):
                        if direction == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = "@"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "@"
                        break


def ship_fits(SHIP_LENGTHS, row, column, direction):
    """
    The ship fits function checks if ships
    placed on the board will fit
    """
    if direction == "H":
        if column + SHIP_LENGTHS > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTHS > 8:
            return False
        else:
            return True


def check_overlap(board, row, column, direction, ship_length):
    """
    The check overlap function will check if any ships placed
    on the board will overlap on other ships
    """
    if direction == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "@":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "@":
                return True
    return False


def player_input(print_ship):
    """
    The player input function allows the player to
    input the row and column they think the computer
    ships are located whilst getting feedback for any
    wrong keys they have entered
    """
    while True:
        try:
            row = input("Enter the row of the ship 1-8: \n")
            if row in '12345678':
                row = int(row) - 1
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid number between 1-8\n")
    while True:
        try:
            column = input("Enter the column of the ship A-H: \n").upper()
            if column not in 'ABCDEFGH':
                print("Enter a valid letter between A-H\n")
            else:
                column = board_coordinates[column]
                break
        except KeyError:
            print("Please enter a valid letter between A-H\n")
    return row, column


def hit_count(board):
    """
    The hit count function will count the number of hits the player
    and computer has taken
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def p_c_turns(board):
    """
    The p c turns function will go through the player
    and the computers turns while giving feedback to player
    with what happened during their turn aswell as the computers turn
    """
    if board == C_BOARD:
        row, column = player_input(C_BOARD)
        if board[row][column] == "O":
            p_c_turns(board)
        elif board[row][column] == "X":
            p_c_turns(board)
        elif C_BOARD[row][column] == "@":
            board[row][column] = "X"
            print_slow("\u001B[32mYou hit a ship!\n\u001B[0m")
        else:
            board[row][column] = "O"
            print_slow("\u001B[34mYou hit empty waters\n\u001B[0m")
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "O":
            p_c_turns(board)
        elif board[row][column] == "X":
            p_c_turns(board)
        elif P_BOARD[row][column] == "@":
            board[row][column] = "X"
            print_slow("\u001B[31mYour ship was hit!\n\u001B[0m")
        else:
            board[row][column] = "O"
            print_slow("\u001B[34mThey hit empty water\n\u001B[0m")


def start_game():
    """
    Start game function
    """
    # Add the ships to each board
    print_ship(P_BOARD)
    print_ship(C_BOARD)

    # Display the players board
    print('Player board\n')
    print_board(P_BOARD)
    # Players turn
    while True:
        # Players turn
        print("Guess the ship coordinates\n")

        # Show the computers current board
        print('Computers board\n')
        print_board(C_BOARD)
        # Carry out the players turn, targeting the computers board
        p_c_turns(C_BOARD)

        if hit_count(C_BOARD) == 17:
            print_slow("\u001B[32mYou sunk all their ships! You win!\
                \n\u001B[0m")
            return play_again()

        # Computers turn
        print('Player board\n')
        # Carry out the computers turn, targeting the players board
        p_c_turns(P_BOARD)
        # Show the players board
        print_board(P_BOARD)

        if hit_count(P_BOARD) == 17:
            print_slow("\u001B[31mThey have sunk all your ships! You lose\
                \n\u001B[0m")
            return play_again()


def play_again():
    """
    The play again function will ask the player
    if they want to play again after the game has ended
    """
    global P_BOARD
    global C_BOARD
    P_BOARD = [[" "] * 8 for i in range(8)]
    C_BOARD = [[" "] * 8 for i in range(8)]
    print_slow("Would you like to play again?\n")
    answer = input("Enter Y or N \n").upper()
    print(' ')
    while True:
        if answer == "Y":
            start_game()
        elif answer == "N":
            print(' ')
            print_slow("Goodbye! See you next time!\n")
            print(' ')
            sys.exit()
        else:
            print(' ')
            print_slow("Please enter Y or N\n")
            answer = input("Enter Y or N \n").upper()


if __name__ == "__main__":
    intro()
    start_game()
