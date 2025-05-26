"""
<<<<<<< HEAD
Step 1: Board Evaluation Function 
=======
الخطوة 1: دالة تقييم اللوحة
>>>>>>> 28927f3a52503b2fe1bd9e81f5737e11704dd448
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
<<<<<<< HEAD
        return '-' 
      
"""
Step 2: Move Function 
(function move)
"""    
def move(board, mark, position):
    if position < 0 or position >= len(board):
        return board  # Invalid position, return the board as is
    
    # Convert the board to a list for easier modification
=======
        return '-'
    
def move(board, mark, position):
    if position < 0 or position >= len(board):
        return board  # الموضع غير صالح، نعيد اللوحة كما هي
    
    # تحويل اللوحة إلى قائمة لتسهيل التعديل
>>>>>>> 28927f3a52503b2fe1bd9e81f5737e11704dd448
    board_list = list(board)
    if board_list[position] == '-':
        board_list[position] = mark
    return ''.join(board_list)

<<<<<<< HEAD
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
        
def improved_pc_move(board, pc_mark):
    player_mark = 'x' if pc_mark == 'o' else 'o'
    board_len = len(board)
    
    # 1. Check if the computer can win in the next move
    for i in range(board_len - 2):
        window = board[i:i+3]
        if window.count(pc_mark) == 2 and window.count('-') == 1:
            pos = i + window.index('-')
            return move(board, pc_mark, pos)
    
    # 2. Block the player from winning in the next move
    for i in range(board_len - 2):
        window = board[i:i+3]
        if window.count(player_mark) == 2 and window.count('-') == 1:
            pos = i + window.index('-')
            return move(board, pc_mark, pos)
    
    # 3. Try to create a winning opportunity (e.g., place two marks with a gap)
    for i in range(board_len - 1):
        if board[i] == pc_mark and board[i+1] == '-':
            return move(board, pc_mark, i+1)
        if board[i] == '-' and board[i+1] == pc_mark:
            return move(board, pc_mark, i)
    
    # 4. Play in the center if available
    center = board_len // 2
    if board[center] == '-':
        return move(board, pc_mark, center)
    
    # 5. Play in any available random position
    return pc_move(board, pc_mark)

if __name__ == "__main__":
    tictactoe_1d()
=======
    
>>>>>>> 28927f3a52503b2fe1bd9e81f5737e11704dd448
