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
