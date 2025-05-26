"""
Step 1: Board Evaluation Function 
(evaluate board)
"""
def evaluate(board):
    # Check if X wins
    if 'xxx' in board:
        return 'x'
    # Check if O wins
    elif 'ooo' in board:
        return 'o'
    # Check for a draw (board is full and no winner)
    elif '-' not in board:
        return '!'
    # Game is not over yet
    else:
        return '-' 
      
"""
Step 2: Move Function 
(function move)
"""    
def move(board, mark, position):
    if position < 0 or position >= len(board):
        return board  # Invalid position, return the board as is
    
    # Convert the board to a list for easier modification
    board_list = list(board)
    if board_list[position] == '-':
        board_list[position] = mark
    return ''.join(board_list)

"""
Step 3: Player Move Function 
(player_move)
"""
def player_move(board, mark):
    while True:
        try:
            position = int(input(f"Enter a position to place '{mark}' (0-19): "))
            if position < 0 or position >= len(board):
                print("Position out of range. Must be between 0 and 19.")
                continue
            if board[position] != '-':
                print("This position is already taken. Choose another position.")
                continue
            return move(board, mark, position)
        except ValueError:
            print("Please enter a valid integer.")

print("NNNNNNNNNNNNN")
import random

def pc_move(board, mark):
    while True:
        position = random.randint(0, len(board)-1)
        if board[position] == '-':
            return move(board, mark, position)
        
def tictactoe_1d():
    # Initialize the board
    board = '-' * 20
    player_mark = 'x'
    pc_mark = 'o'
    
    print("Welcome to 1D Tic Tac Toe!")
    print("You are playing as 'x' and the computer as 'o'.")
    print("Current board:", board)
    
    while True:
        # Player's turn
        board = player_move(board, player_mark)
        print("Board after your move:", board)
        
        # Check game status
        result = evaluate(board)
        if result == player_mark:
            print("Congratulations! You won!")
            return
        elif result == pc_mark:
            print("You lost! The computer won.")
            return
        elif result == '!':
            print("It's a draw! The board is full and no one won.")
            return
        
        # Computer's turn
        print("Computer's turn to play...")
        board = pc_move(board, pc_mark)
        print("Board after computer's move:", board)
        
        # Check game status
        result = evaluate(board)
        if result == player_mark:
            print("Congratulations! You won!")
            return
        elif result == pc_mark:
            print("You lost! The computer won.")
            return
        elif result == '!':
            print("It's a draw! The board is full and no one won.")
            return