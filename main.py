"""
Tic Tac Toe Game is a 2 player Board game. 
"""

# Board for the game - with 10 spaces. BOARD[0] will be ignored
BOARD = [' ' for x in range(10)]

# Define Functions to play the Game Logic
def play_game():
    """
    play_game
    Holds all the functions required to run the game.
    """
    print("Welcome to Tic-Tac-Toe! You're 'X' and the Computer is 'O'.")
    
    # Display initial Board
    display_board()

    while not(isBoardFull(BOARD)):
        # check if player 0 - the computer has not won.
        if not(isWinner(BOARD, 'O')):
            handlePlayerTurn()
            display_board()
        else:
            print("You Lost! 'O' is the Winner!! - ComputerWork")
            break
        
        # Check if player X - You, has not won.
        if not(isWinner(BOARD, 'X')):
            computer_play_this_position = handleComputerTurn()
            if computer_play_this_position == 0:
                print("XO Draw!")
            else:
                playThisPosition('O', computer_play_this_position)
                print("Nice Move Computer. Computer placed an 'O' in postion", computer_play_this_position , ":")
                display_board()
        else:
            print("You're a Winner! You've won the Computer! Good Job :)")
            break

def display_board():
    """
    display_board
    Shows the Game BOARD to the screen
    """
    print()
    print('-------------')
    print('| ' + BOARD[1] + ' | ' + BOARD[2] + ' | ' + BOARD[3] + ' |')
    print('-------------')
    print('| ' + BOARD[4] + ' | ' + BOARD[5] + ' | ' + BOARD[6] + ' |')
    print('-------------')
    print('| ' + BOARD[7] + ' | ' + BOARD[8] + ' | ' + BOARD[9] + ' |')
    print('-------------')
    print()


def spaceIsFree(pos):
    return BOARD[pos] == ' '


def playThisPosition(player_symbol, pos):
    BOARD[pos] = player_symbol


def handlePlayerTurn():
    """
    handlePlayerTurn
    Handle a player's turn to play a move. 
    """
    # Check validity of the input from the user (player), and make sure the spot on the board is open. 
    play = True
    while play:
        # The positions on the Board
        position = input("Choose a position to place an 'X', from (1-9): ")
        try:
            position = int(position)
            if position > 0 and position < 10:
                if spaceIsFree(position):
                    playThisPosition('X', position)
                    play = False
                else:
                    print("This position is occupied. Play again.")
            else:
                print("Please type a number within the range (1 - 9)")
        except:
            print("Please type a number from (1 -9)!")


def handleComputerTurn():
    # The computer can only place an O in an empty spot.
    possiblePositions = [x for x, player_symbol in enumerate(BOARD) if player_symbol == ' ' and x != 0]

    postion = 0

    # Check if there is a winner first.
    for symbol in ['O', 'X']:
        for i in possiblePositions:
            BOARDCLONE = BOARD[:]
            BOARDCLONE[i] = symbol
            if isWinner(BOARDCLONE, symbol):
                postion = i
                return postion
    
    # check corners of the board and randomly play a position
    boardCornersOpen = []
    for i in possiblePositions:
        if i in [1, 3, 7, 9]:
            boardCornersOpen.append(i)
    if len(boardCornersOpen) > 0:
        postion = playThisRandomPosition(boardCornersOpen)
        return postion
    
    # check center of the board and play the center
    if 5 in possiblePositions:
        postion = 5
        return postion
    
    # check the edges of the board and randomly play a position
    boardEdgesOpen = []
    for i in possiblePositions:
        if i in [2, 4, 6, 8]:
            boardEdgesOpen.append(i)
    if len(boardEdgesOpen) > 0:
        postion = playThisRandomPosition(boardEdgesOpen)
    
    return postion


def isWinner(board, player_symbol):
    # check rows or # check columns or # check diagonals

    return (board[7] == player_symbol and board[8] == player_symbol and board[9] == player_symbol) or \
        (board[4] == player_symbol and board[5] == player_symbol and board[6] == player_symbol) or \
        (board[1] == player_symbol and board[2] == player_symbol and board[3] == player_symbol) or \
        (board[1] == player_symbol and board[4] == player_symbol and board[7] == player_symbol) or \
        (board[2] == player_symbol and board[5] == player_symbol and board[8] == player_symbol) or \
        (board[3] == player_symbol and board[6] == player_symbol and board[9] == player_symbol) or \
        (board[1] == player_symbol and board[5] == player_symbol and board[9] == player_symbol) or \
        (board[3] == player_symbol and board[5] == player_symbol and board[7] == player_symbol)


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def playThisRandomPosition(lst):
    import random
    length_list = len(lst)
    randomPosition = random.randrange(0, length_list)
    return lst[randomPosition]

# Start Game
play_game()
