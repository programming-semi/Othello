# 定数宣言
BLANK = 0
BLACK = 1
WHITE = -1
WALL = 2
CAN_PUT = 3
SWITCH_COLOR = -1

def board_print(board):
    # 初期化：
    print_board = [
            [WALL, WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL],
            [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
            [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
            [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
            [WALL, BLANK, BLANK, BLANK, BLACK, WHITE, BLANK, BLANK, BLANK, WALL],
            [WALL, BLANK, BLANK, BLANK, WHITE, BLACK, BLANK, BLANK, BLANK, WALL],
            [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
            [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
            [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
            [WALL, WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL]]

    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == WHITE:
                print_board[i][j] = '○'
            elif board[i][j] == BLACK:
                print_board[i][j] = '●'
            elif board[i][j] == CAN_PUT:
                print_board[i][j] = '☆'
            else:
                print_board[i][j] = ' '

    # print_boardを利用してオセロを表示
    print("\n\t   1 2 3 4 5 6 7 8")
    print("\t  +---------------+")
    for i in range(1, 9):
        print("\t" + str(i), end=" ")
        for j in range(1, 9):
            print('|'+print_board[i][j], end="")
        print('|')
    print("\t  +---------------+\n")
