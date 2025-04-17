"""
الخطوة 1: دالة تقييم اللوحة
(evaluate board)
"""
def evaluate(board):
    # التحقق من فوز X
    if 'xxx' in board:
        return 'x'
    # التحقق من فوز O
    elif 'ooo' in board:
        return 'o'
    # التحقق من التعادل (اللوحة ممتلئة ولا يوجد فائز)
    elif '-' not in board:
        return '!'
    # اللعبة لم تنته بعد
    else:
        return '-'
    
def move(board, mark, position):
    if position < 0 or position >= len(board):
        return board  # الموضع غير صالح، نعيد اللوحة كما هي
    
    # تحويل اللوحة إلى قائمة لتسهيل التعديل
    board_list = list(board)
    if board_list[position] == '-':
        board_list[position] = mark
    return ''.join(board_list)

    