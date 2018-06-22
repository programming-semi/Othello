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

# モジュールをインポート
## 標準 (?) モジュール
import numpy
import pprint
import sys
## かなさんモジュール
import board_print_kurihara

# 定数宣言
BLANK = 0
BLACK = 1
WHITE = -1
WALL = 2
CAN_PUT = 3
SWITCH_COLOR = -1

# 盤面生成
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

my_color = BLACK        # プレイヤー 1 の色
opponent_color = WHITE  # プレイヤー 2 の色
pass_count = 0          # パスが何回行われたか (2 回連続でパスが行われたらゲーム終了)

# 2 連続パスが行われるまでゲームを続ける
while pass_count < 2:

    # 置けるかどうかのチェック
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

    # 置ける場所があったかどうかを変数へ格納 (置ける場所が一箇所でもあれば OK)．
    can_put_flag = False    # 置ける場所があるかどうかのフラグ: 一箇所でもあればとりあえず OK
    for i in range(1, 9):
        if can_put_flag == True:
            break
        for j in range(1, 9):
            if board[i][j] == CAN_PUT:
                can_put_flag = True
                pass_count = 0
                break

    # どこにも置けない ==> ターンを交代して，pass を 1 増やし，上の while へ戻る
    if can_put_flag == False:
        my_color = my_color * SWITCH_COLOR
        opponent_color = opponent_color * SWITCH_COLOR
        pass_count += 1 # <==> pass_count = pass_count + 1
        continue        # 現在のスコープから抜けて，そのスコープのスタート (while, for など) に戻って，命令を繰り返す

    # (置ける場所を追加した後の) 盤面を表示
    board_print_kurihara.board_print(board)

    # 現在の色を確認
    print('> あなたの石色: ', end='')   # python3.X における記述方法 (2.X だとこのような記述はできないっぽい)
    if my_color == BLACK:
        print('● (黒)')
    else:
        print('◯ (白)')

    # キーボードから入力させる
    print("> 石を置きたい「行」を指定してください (例：4)")
    stone_row = input()
    print("> 石を置きたい「列」を指定してください (例：3)")
    stone_col = input()

    # 入力された値を int 型へキャスト
    p = int(stone_row)
    q = int(stone_col)

    # キーボードから入力された値が置ける場所であれば，if 以下を実行
    if board[p][q] == CAN_PUT:
        # 指定された場所 (p, q) へ置く
        print("> " + str(p) + "行" + str(q) + "列目に石を置きます")
        board[p][q] = my_color

        # 置いた後は，置ける場所 (CAN_PUT) は全て削除
        for i in range(1, 9):
            for j in range(1, 9):
                if board[i][j] == CAN_PUT:
                    board[i][j] = BLANK

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

        # (置いてひっくり返したあとの) 盤面を表示
        board_print_kurihara.board_print(board)

        # プレイヤー交代
        my_color = my_color * SWITCH_COLOR
        opponent_color = opponent_color * SWITCH_COLOR
        print("> プレイヤーを交代してください")

    # キーボードから入力された値が置けない場所 (i.e., !CAN_PUT) だったとき
    else:
        print("> ごめんなさい，そのマスには置けません．石を置き直してください")
        # このときに処理どうしよう ...


# ゲーム終了 (while を抜けた ==> pass_cnt > 2 ==> 置ける場所がない ==> 対局終了)
print("> 置ける場所が無くなりました．対局を終了します")

# カウンター 2 つ
black_count = 0
white_count = 0

# コマを数え上げる
for i in range(1, 9):
    for j in range(1, 9):
        if board[i][j] == BLACK:
            black_count += 1
        elif board[i][j] == WHITE:
            white_count += 1

# コマの総数を比較
if black_count < white_count:
    print("> 後攻プレイヤー (白) の勝ち")
elif black_count > white_count:
    print("> 先攻プレイヤー (黒) の勝ち")
else:
    print("> 引き分けだよ")
