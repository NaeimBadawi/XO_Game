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