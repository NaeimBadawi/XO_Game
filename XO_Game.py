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
    