"""
Tic Tac Toe Game is a 2 player Board game. 
"""

# Global variables

# Board for the game
BOARD = ["_", "_", "_",
        "_", "_", "_", 
        "_", "_", "_"]

# If game is still on
GAME_STILL_ON = True

# And the WINNER is
WINNER = None

# Switch Player, First player will be X, and second player will be O. X will start to play
CURRENT_PLAYER = "X"


# Define Functions to play the Game Logic

"""
play_game
Holds all the functions required to run the game.
"""
def play_game():

    # Display initial Board
    display_board()

    # Game loop
    while GAME_STILL_ON:

        # handle a single turn of an arbitrary player
        handle_turn(CURRENT_PLAYER)

        # Check if the game has ended
        check_if_game_over()

        # Switch to the other player
        switch_player()
    
    # Check if the Winner is X or O.
    if WINNER == "X" or WINNER == "O":
        print(WINNER + " is the Winner!!")
    elif WINNER == None:
        print("XO Draw!")

"""
display_board
Shows the Game BOARD to the screen
"""
def display_board():
    print()
    print(BOARD[0] + " | " + BOARD[1] + " | " + BOARD[2])
    print(BOARD[3] + " | " + BOARD[4] + " | " + BOARD[5])
    print(BOARD[6] + " | " + BOARD[7] + " | " + BOARD[8])
    print()

"""
handle_turn
Handle a player's turn. 
@param: string
The current player is a string ("X" or "O")
"""
def handle_turn(player):

    # Get the position from the player
    print(player + "'s turn.")
    position = input("Choose a postion from 1 - 9: ")

    # Check validity of the input from the user (player), and make sure the spot on the board is open. 
    valid = False
    while not valid:
        # The positions on the Board
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a postion from 1 - 9: ")

        # Correct index on the Board
        position = int(position) - 1

        # spot choose must be available on the Board
        if BOARD[position] == "_":
            valid = True
        else:
            print("You can't play this spot. Play again.")

    # input the player variable to the choosen spot
    BOARD[position] = player
    display_board()



"""
check_if_game_over
Check if there is a game over
"""
def check_if_game_over():
    check_if_winner()
    check_if_tie()


"""
check_if_winner
Check if someone has won
"""
def check_if_winner():
    
    global WINNER

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        WINNER = row_winner
    elif column_winner:
        WINNER = column_winner
    elif diagonal_winner:
        WINNER = diagonal_winner
    else:
        WINNER = None
    return


"""
check_rows
checks the rows for a win
"""
def check_rows():
    # set up global variables
    global GAME_STILL_ON
    # check if any of the rows have all the same value (and is not empty)
    row_1 = BOARD[0] == BOARD[1] == BOARD[2] != "_"
    row_2 = BOARD[3] == BOARD[4] == BOARD[5] != "_"
    row_3 = BOARD[6] == BOARD[7] == BOARD[8] != "_"
    # if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        GAME_STILL_ON = False
    # Return the winner (X or O)
    if row_1:
        return BOARD[0]
    elif row_2:
        return BOARD[3]
    elif row_3:
        return BOARD[6]
    return


"""
check_columns
checks the cloumns for a win
"""
def check_columns():
    # set up global variables
    global GAME_STILL_ON
    # check if any of the rows have all the same value (and is not empty)
    column_1 = BOARD[0] == BOARD[3] == BOARD[6] != "_"
    column_2 = BOARD[1] == BOARD[4] == BOARD[7] != "_"
    column_3 = BOARD[2] == BOARD[5] == BOARD[8] != "_"
    # if any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        GAME_STILL_ON = False
    # Return the winner (X or O)
    if column_1:
        return BOARD[0]
    elif column_2:
        return BOARD[1]
    elif column_3:
        return BOARD[2]
    return


"""
check_diagonals
checks the diagonals for a win
"""
def check_diagonals():
    # set up global variables
    global GAME_STILL_ON
    # check if any of the rows have all the same value (and is not empty)
    diagonal_1 = BOARD[0] == BOARD[4] == BOARD[8] != "_"
    diagonal_2 = BOARD[6] == BOARD[4] == BOARD[2] != "_"
    # if any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        GAME_STILL_ON = False
    # Return the winner (X or O)
    if diagonal_1:
        return BOARD[0]
    elif diagonal_2:
        return BOARD[6]
    return

def check_if_tie():
    global GAME_STILL_ON
    if "_" not in BOARD:
        GAME_STILL_ON = False
    return

"""
switch_player
changes player to take their turn
"""
def switch_player():
    # global variables we need
    global CURRENT_PLAYER

    # if the current player is X, change it to O
    if CURRENT_PLAYER == "X":
        CURRENT_PLAYER = "O"
        # if the current player is 0, change it to x
    elif CURRENT_PLAYER == "O":
        CURRENT_PLAYER = "X"
    return

# Start Game
play_game()
