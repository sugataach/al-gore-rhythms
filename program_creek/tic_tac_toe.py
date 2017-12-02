def vWin(player, board):
    n = len(board[0])
    for col in range(n):
        has_col = True
        for row in range(n):
            if board[row][col] != player:
                has_col = False
                break
        if has_col:
            return True
    return False

def hWin(player, board):
    n = len(board[0])
    for row in range(n):
        has_row = True
        for col in range(n):
            if board[row][col] != player:
                has_row = False
                break
        if has_row:
            return True
    return False

def dWin(player, board):
    d1 = [(0,0),(1,1),(2,2)]
    d2 = [(0,2),(1,1),(2,0)]
    has_dwin1 = True
    has_dwin2 = True
    for val in d1:
        if board[val[0]][val[1]] != player:
            has_dwin1 = False
    for val in d2:
        if board[val[0]][val[1]] != player:
            has_dwin2 = False
    return has_dwin1 or has_dwin2

def check_win(player, board):
    if vWin(player, board) or hWin(player, board) or dWin(player, board):
        return True
    return False

player = 'X'
board = [
    ['X','-','-'],
    ['O','X','-'],
    ['O','-','X']
]

print(check_win(player, board))
