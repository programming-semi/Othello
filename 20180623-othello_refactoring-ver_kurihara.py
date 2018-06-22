# -*- coding: utf-8 -*-

#
# [20180618]
#        ひとまず，動くやつを作った (20180623 にプレゼン予定)
#        あと，やるとすれば ...
#                 - かなさんの <8direction> を使う
#                 - 各処理を関数化する
#                 - 各変数に適切な名前をつける
#                 - エラー処理を真面目に書く (e.g. 現状，キーボードから番外 (e.g. 100行100列) を指定すると，エラー吐いてプログラムが終了する)
#
#        「このプログラムがオセロとしてちゃんと遊べるかどうか」という意味では，たぶん OK
#        「プログラムが読みやすいか，拡張性 (機能を追加したり，変更したりしやすいか) があるかどうか」という意味では NG
#                 # 変数名が分かりづらかったり，関数化されてなかったり，エラー処理がちゃんとできていなかったりなど ...
#
#        !! <board_print_kurihara.py> とセットでこのプログラムを使ってください
#
#
# [20180622]
#       やったこと: リファクタリング
#           関数をたくさん作って，main 文から sub の関数を呼び出す形になっている
#               - 全体を通して (たぶん) 読みやすくなる
#               - 機能をひとまとめにして名前をつけている (i.e., 関数) ので，名前を呼び出せば，その命令が実行される
#                   ==> 再利用可能
#               - main 文から切り離せれば (独立させれば)，関数 (一機能) 単位での変更がくわえやすい
#                   ==> メンテナンスしやすい
#

# モジュールをインポート
## かなさんモジュール
import board_print_kurihara

#
# sub functions
#

# 盤面生成
def createBoard():

    board = [[WALL, WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL],
             [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
             [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
             [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
             [WALL, BLANK, BLANK, BLANK, WHITE, BLACK, BLANK, BLANK, BLANK, WALL],
             [WALL, BLANK, BLANK, BLANK, BLACK, WHITE, BLANK, BLANK, BLANK, WALL],
             [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
             [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
             [WALL, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL],
             [WALL, WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL]]

    # board = [[WALL, WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL],
    #          [WALL, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, WALL],
    #          [WALL, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, WALL],
    #          [WALL, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, WHITE, WALL],
    #          [WALL, BLACK, BLACK, BLANK, WHITE, BLACK, BLANK, BLANK, BLANK, WALL],
    #          [WALL, BLACK, BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, WALL],
    #          [WALL, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, WALL],
    #          [WALL, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, WALL],
    #          [WALL, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, WALL],
    #          [WALL, WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL,  WALL]]

    return board


# 置けるかどうかのチェック
def canPutBoard(board):

    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == my_color:

                # 右方向をチェック
                if board[i][j+1] == opponent_color:
                    k = 1
                    while board[i][j+k] == opponent_color:
                        k = k+1
                    else:
                        if board[i][j+k] == BLANK:
                            board[i][j+k] = CAN_PUT

                # 右下方向をチェック
                if board[i+1][j+1] == opponent_color:
                    k = 1
                    while board[i+k][j+k] == opponent_color:
                        k = k+1
                    else:
                        if board[i+k][j+k] == BLANK:
                            board[i+k][j+k] = CAN_PUT

                # 下方向をチェック
                if board[i+1][j] == opponent_color:
                    k = 1
                    while board[i+k][j] == opponent_color:
                        k = k+1
                    else:
                        if board[i+k][j] == BLANK:
                            board[i+k][j] = CAN_PUT

                # 左下方向をチェック
                if board[i+1][j-1] == opponent_color:
                    k = 1
                    while board[i+k][j-k] == opponent_color:
                        k = k+1
                    else:
                        if board[i+k][j-k] == BLANK:
                            board[i+k][j-k] = CAN_PUT

                # 左方向をチェック
                if board[i][j-1] == opponent_color:
                    k = 1
                    while board[i][j-k] == opponent_color:
                        k = k+1
                    else:
                        if board[i][j-k] == BLANK:
                            board[i][j-k] = CAN_PUT

                # 左上方向をチェック
                if board[i-1][j-1] == opponent_color:
                    k = 1
                    while board[i-k][j-k] == opponent_color:
                        k = k+1
                    else:
                        if board[i-k][j-k] == BLANK:
                            board[i-k][j-k] = CAN_PUT

                # 上方向をチェック
                if board[i-1][j] == opponent_color:
                    k = 1
                    while board[i-k][j] == opponent_color:
                        k = k+1
                    else:
                        if board[i-k][j] == BLANK:
                            board[i-k][j] = CAN_PUT

                # 右上方向をチェック
                if board[i-1][j+1] == opponent_color:
                    k = 1
                    while board[i-k][j+k] == opponent_color:
                        k = k+1
                    else:
                        if board[i-k][j+k] == BLANK:
                            board[i-k][j+k] = CAN_PUT
    return board


# 置ける場所 (CAN_PUT) があるかどうかをチェック
def checkCanPutFlag(can_put_flag):

    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == CAN_PUT:
                can_put_flag = True
                pass_count = 0
                return can_put_flag

    return can_put_flag


# キーボードから入力させる
def inputPoint():

    print("> 石を置きたい「行」を指定してください (例：4)")
    stone_row = int(input())
    print("> 石を置きたい「列」を指定してください (例：3)")
    stone_col = int(input())

    return stone_row, stone_col


# 現在の色を確認
def printNowColor(my_color, BLACK):

    print('> あなたの石色: ', end='')   # python3.X における記述方法 (2.X だとこのような記述はできないっぽい)
    if my_color == BLACK:
        print('● (黒)')
    else:
        print('◯ (白)')


def flipPieces(board, my_color, opponent_color, p, q):

    # 右上方向へひっくり返せる場所を探し，可能であればひっくり返す．
    if board[p-1][q+1] == opponent_color:
        k = p-1
        l = q+1
        while board[k][l] == opponent_color: # 見ている座標の位置を各方向ごとにずらしています
            k = k-1
            l = l+1
            if board[k][l] == my_color: # 相手の色が続いた先に自分の色があったなら
                m = p-1
                n = q+1
                while m >= k and n <= l: # mが自分の色があるマスまで(上のwhile文が終了したlまで)
                    board[m][n] = my_color
                    m = m-1
                    n = n+1

    # 右方向へひっくり返せる場所を探し，可能であればひっくり返す．
    if board[p][q+1] == opponent_color:
        k = p
        l = q+1
        while board[k][l] == opponent_color:
            l = l+1
            if board[k][l] == my_color:
                n = q+1
                while n <= l:
                    board[k][n] = my_color
                    n = n+1

    # 右下方向へひっくり返せる場所を探し，可能であればひっくり返す．
    if board[p+1][q+1] == opponent_color:
        k = p+1
        l = q+1
        while board[k][l] == opponent_color:
            k = k+1
            l = l+1
            if board[k][l] == my_color:
                m = p+1
                n = q+1
                while m <= k and n <= l:
                    board[m][n] = my_color
                    n = n+1
                    m = m+1

    # 左上方向へひっくり返せる場所を探し，可能であればひっくり返す．
    if board[p-1][q-1] == opponent_color:
        k = p-1
        l = q-1
        while board[k][l] == opponent_color:
            k = k-1
            l = l-1
            if board[k][l] == my_color:
                m = p-1
                n = q-1
                while m >= k and n >= l:
                    board[m][n] = my_color
                    n = n-1
                    m = m-1

    # 左方向へひっくり返せる場所を探し，可能であればひっくり返す．
    if board[p][q-1] == opponent_color:
        k = p
        l = q-1
        while board[k][l] == opponent_color:
            l = l-1
            if board[k][l] == my_color:
                n = q-1
                while n >= l:
                    board[k][n] = my_color
                    n = n-1

    # 左下方向へひっくり返せる場所を探し，可能であればひっくり返す．
    if board[p+1][q-1] == opponent_color:
        k = p+1
        l = q-1
        while board[k][l] == opponent_color:
            k = k+1
            l = l-1
            if board[k][l] == my_color:
                m = p+1
                n = q-1
                while m <= k and n >= l:
                    board[m][n] = my_color
                    m = m+1
                    n = n-1

    # 下方向へひっくり返せる場所を探し，可能であればひっくり返す．
    if board[p+1][q] == opponent_color:
        k = p+1
        l = q
        while board[k][l] == opponent_color:
            k = k+1
            l = l
            if board[k][l] == my_color:
                m = p+1
                n = q
                while m <= k:
                    board[m][n] = my_color
                    m = m+1
                    n = n

    # 上方向へひっくり返せる場所を探し，可能であればひっくり返す．
    if board[p-1][q] == opponent_color:
        k = p-1
        l = q
        while board[k][l] == opponent_color:
            k = k-1
            l = l
            if board[k][l] == my_color:
                m = p-1
                n = q
                while m >= k:
                    board[m][n] = my_color
                    m = m-1
                    n = n

    return board


# プレイヤー交代
def switchColor(my_color, opponent_color):

    print("> プレイヤーを交代してください")

    my_color = my_color * SWITCH_COLOR
    opponent_color = opponent_color * SWITCH_COLOR

    return my_color, opponent_color


# 置いた後は，置ける場所 (CAN_PUT) は全て削除
def deleteCanPutMark(board):

    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == CAN_PUT:
                board[i][j] = BLANK


# 盤上のコマを全て数え上げる
def countTotalPiece(black_count, white_count):

    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == BLACK:
                black_count += 1
            elif board[i][j] == WHITE:
                white_count += 1

    return black_count, white_count


# コマの総数を比較して，勝者決定
def compareTotalPieces(black_count, white_count):

    if black_count < white_count:
        print("> 後攻プレイヤー (白) の勝ち")
    elif black_count > white_count:
        print("> 先攻プレイヤー (黒) の勝ち")
    else:
        print("> 引き分けだよ")


# 以下，main function

# 定数宣言 (小文字でも良いが，変数と区別する為，大文字にしている (習慣))
BLANK = 0
BLACK = 1
WHITE = -1
WALL = 2
CAN_PUT = 3
SWITCH_COLOR = -1

# 変数初期化 (主に while 内で使用する変数たち)
board = createBoard()
my_color = BLACK
opponent_color = WHITE
pass_count = 0

while pass_count < 2: # 以下，2 連続パスが行われるまでゲームを続ける

    canPutBoard(board) # 置ける場所があれば，そこに印をつける (==> 名前は markCanPut の方が適切 ?)

    can_put_flag = checkCanPutFlag(can_put_flag=False)  # 置ける場所があったかどうか (置ける場所が一箇所でもあれば OK)．
                                                        # [check: 確認する] ==> 表現が曖昧であまり良くないかも
    if can_put_flag == False: # どこにも置けない ==> ターンを交代して，pass を 1 増やし，while へ戻る (continue する)
        my_color, opponent_color = switchColor(my_color, opponent_color)    # 色を変えて，その結果を持ち帰って変数へ代入
        pass_count += 1
        continue

    board_print_kurihara.board_print(board) # 盤面を表示
    printNowColor(my_color, BLACK)          # 順番 (どちらのターンか) を表示

    p, q = inputPoint()         # 座標をキーボードから入力
    if board[p][q] == CAN_PUT:  # キーボードから入力された座標が置ける場所だったら，いろいろ (if 文内) やる
        print("> " + str(p) + "行" + str(q) + "列目に石を置きます")         # ただの print
        board[p][q] = my_color                                              # コマ置いて ...
        deleteCanPutMark(board)                                             # つけた印 (CAN_PUT) を削除して ...
        flipPieces(board, my_color, opponent_color, p, q)                   # ひっくり返して ...
        my_color, opponent_color = switchColor(my_color, opponent_color)    # コマの色 (プレイヤー) を交代
    else:
        print("> ごめんなさい，そのマスには置けません．石を置き直してください")


# 対局終了 (while を抜けた ==> pass_cnt > 2 ==> 置ける場所がない ==> 対局終了)
print("> 置ける場所が無くなりました．対局を終了します")                     # ただの print
black_count, white_count = countTotalPiece(black_count=0, white_count=0)    # コマの総数を数え上げて，変数へ代入
compareTotalPieces(black_count, white_count)                                # 結果を比較 ==> 勝者決定
board_print_kurihara.board_print(board)
