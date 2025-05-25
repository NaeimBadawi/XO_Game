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
