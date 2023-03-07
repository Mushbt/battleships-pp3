import random

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


# Game introduction
def intro():
    print("Welcome to battleships!\n")
    print("Battleships is a strategy type guessing game\n")
    print("It is played on a ruled grid (In this case 8x8)\n")
    print("You and the computer will have 5 ships each with different sizes\n")
    print("The location of the ships will be concealed from each other\n")
    print("You will take turns calling coordinates trying to sink eachothers \
ships\n")
    print("The objective of the game is to try and sink all the computers \
ships\n")
    print("When this has been achieved bu either you or the computer, the game\
will be over")

    # Ships and sizes
    print("You will have the following ships in your fleet:\n")
    print("DESTROYER - 2 BOARD POSITIONS")
    print("SUBMARINE - 3 BOARD POSITIONS")
    print("CRUISER - 3 BOARD POSITIONS")
    print("BATTLESHIP -  4 BOARD POSITIONS")
    print("CARRIER - 5 BOARD POSITIONS")

    # Game legend
    print("The following is the game legend:")
    print("@ - SHIP")
    print("O - MISSED TARGET")
    print("X - HIT TARGET")


def print_board(board):
    """
    The print board function prints out the game board
    """
    print(' A B C D E F G H')
    print(' ***************')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
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
            print("Please enter a valid number between 1-8")
    while True:
        try:
            column = input("Enter the column of the ship A-H: \n").upper()
            if column not in 'ABCDEFGH':
                print("Enter a valid letter between A-H")
            else:
                column = board_coordinates[column]
                break
        except KeyError:
            print("Please enter a valid letter between A-H")
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
    with what happened durint their turn aswell as the computers turn
    """
    if board == P_BOARD:
        row, column = player_input(P_BOARD)
        if board[row][column] == "O":
            p_c_turns(board)
        elif board[row][column] == "X":
            p_c_turns(board)
        elif C_BOARD[row][column] == "@":
            board[row][column] = "X"
            print("You hit a ship!\n")
        else:
            board[row][column] = "O"
            print("You hit empty waters\n")
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "O":
            p_c_turns(board)
        elif board[row][column] == "X":
            p_c_turns(board)
        elif P_BOARD[row][column] == "@":
            board[row][column] = "X"
            print("You ship was hit!")
        else:
            board[row][column] = "O"
            print("They hit empty water")


def start_game():
    """
    Start game function
    """
    print_ship(C_BOARD)
    print_board(P_BOARD)
    print_ship(P_BOARD)
    # Players turn
    while True:
        print("Guess the ship coordinates\n")
        print_board(P_BOARD)
        p_c_turns(P_BOARD)
        if hit_count(P_BOARD) == 17:
            print("You sunk all their ships! You win!")
            break

    # Computers turn
        p_c_turns(C_BOARD)
        print_board(C_BOARD)
        if hit_count(C_BOARD) == 17:
            print("They have sunk all your ships! You lose")
            break


def play_again():
    """
    The play again function will ask the player
    if they want to play again after the game has ended
    """
    print("Would you like to play again?\n")
    answer = input("Enter Y or N \n").upper()
    print(' ')
    while True:
        if answer == "Y":
            intro()
        elif answer == "N":
            print(' ')
            print("Goodbye! See you next time!")
            print(' ')
            return False
            intro()
        else:
            print(' ')
            print("Pleas enter Y or N")
            answer = input("Enter Y or N \n").upper()


if __name__ == "__main__":
    intro()
    start_game()
    play_again()