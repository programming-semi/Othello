
# できてから、より効率の良い方法を考える

# ----------------------------------------

# -- board --

# 色情報の入った8x8の行列 で再現すれば、なんとかなりそう
# 色情報が、操作によってどんどん更新されていく

# 色：整数で表現
#	別に"kuro"とか"shiro"でもいいんだろうけど、利便性を考えて
# 1 : 黒, 2 : 白, 0 : 何もいない

# 行列：リスト(ベクトルみたいなやつ、中にデータを入れられる) を使う
#	リストの中にリストを入れることで、「行列」のようなものが再現可能
# 	某Deep learningの本曰く、Numpy?というモジュールが便利らしい
# list=[1,2,3,4,5]のように定義, list[0]とやると、1番目が取り出せる

# とりあえず、初期boardの生成
board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

# 最初の石の色の定義(どちらの番か)
# BLACK = 1
# my_color = BLACK
my_color = 1
#この変数の値はどんどん変わっていく

# このままだと死ぬほど見辛い
# print(board)


# ----------------------------------------

# -- boardの表示 --


# このboard行列のデータをいい感じに操作して、オセロっぽく表示する関数を作ってみた(以下)

import board_print # "オセロ表示"関数 を定義している モジュールのインポート
board_print.board_print(board) # 現在のboardを表示してくれるよ
	# 厳密に言うと8x8行列を与えると、各要素に対して、1ならば●、2ならば○、どちらでもないならば" "を、いい感じにデザインして表示

# ----------------------------------------


# -- 置ける場所をチェックする --

# 今の石状況を見て、置けるマスの行と列を返す

# --

# 0. 相手の色の定義(この位置でいいかはちょっと考える)
opponent_color = 3-my_color


# 1. 隣に相手の色があり、かつ、まだ何もないマスを抽出する(赤フローチャートの最初の分岐をクリアするもの)

# 1-1. 相手の色のマスを全て抽出

opponent_cell = [] # 他の色があるマス
for i in range(8): 
	for j in range(8):
		if board[i][j] == opponent_color:
			opponent_cell.append([i,j])
# print('他の色があるマス：')
# print(opponent_cell)


# 1-2. 各マスに対し、その1つ周りのマスを全て抽出
around_opp_cell = [] # opponent_cellの周り8マスを持ってくる(重複がありうる)

for i in range(len(opponent_cell)):
	around_opp_cell.append([opponent_cell[i][0]-1,opponent_cell[i][1]-1])
	around_opp_cell.append([opponent_cell[i][0]-1,opponent_cell[i][1]])
	around_opp_cell.append([opponent_cell[i][0]-1,opponent_cell[i][1]+1])
	around_opp_cell.append([opponent_cell[i][0],opponent_cell[i][1]-1])
	around_opp_cell.append([opponent_cell[i][0],opponent_cell[i][1]+1])
	around_opp_cell.append([opponent_cell[i][0]+1,opponent_cell[i][1]-1])
	around_opp_cell.append([opponent_cell[i][0]+1,opponent_cell[i][1]])
	around_opp_cell.append([opponent_cell[i][0]+1,opponent_cell[i][1]+1])

# print('各マスに対し、その1つ周りのマス：')
# print(around_opp_cell)

# 1-3. これのうち、すでに石のあるマスを削除

aro_nostone_cell = [] # 石がないところ

for i in range(len(around_opp_cell)):
	if board[around_opp_cell[i][0]][around_opp_cell[i][1]] == 0:
		aro_nostone_cell.append(around_opp_cell[i])

# print('これのうち、すでに石のあるマスを削除')
# print(aro_nostone_cell)

# 1-4. 1-2の和集合を取る

aro_uniq_cell = [] # 1.で欲しかったもの(aro_nostone_cellは重複がありうる)
for x in aro_nostone_cell:
    if x not in aro_uniq_cell:
        aro_uniq_cell.append(x)

# print('重複を削除')
# print(aro_uniq_cell)

# 2. aro_uniq_cellの各マスに対し、のりちゃんと決めたアルゴリズムを適用

# 2-1. aro_uniq_cellは、隣に違う色はすでにあるので、その先に元の色があるかどうか
ok_cell_rep = [] # 完全にOKなマス(uniqじゃない, rep(被り)ある, 1マス分しか見てないです)
for i in range(len(aro_uniq_cell)): 
	if board[aro_uniq_cell[i][0]-1][aro_uniq_cell[i][1]-1] == opponent_color:
		if board [aro_uniq_cell[i][0]-2][aro_uniq_cell[i][1]-2] == my_color:
			ok_cell_rep.append(aro_uniq_cell[i])
	if board[aro_uniq_cell[i][0]][aro_uniq_cell[i][1]-1] == opponent_color:
		if board [aro_uniq_cell[i][0]][aro_uniq_cell[i][1]-2] == my_color:
			ok_cell_rep.append(aro_uniq_cell[i])
	if board[aro_uniq_cell[i][0]+1][aro_uniq_cell[i][1]-1] == opponent_color:
		if board [aro_uniq_cell[i][0]+2][aro_uniq_cell[i][1]-2] == my_color:
			ok_cell_rep.append(aro_uniq_cell[i])
	if board[aro_uniq_cell[i][0]-1][aro_uniq_cell[i][1]] == opponent_color:
		if board [aro_uniq_cell[i][0]-2][aro_uniq_cell[i][1]] == my_color:
			ok_cell_rep.append(aro_uniq_cell[i])
	if board[aro_uniq_cell[i][0]+1][aro_uniq_cell[i][1]] == opponent_color:
		if board [aro_uniq_cell[i][0]+2][aro_uniq_cell[i][1]] == my_color:
			ok_cell_rep.append(aro_uniq_cell[i])
	if board[aro_uniq_cell[i][0]-1][aro_uniq_cell[i][1]+1] == opponent_color:
		if board [aro_uniq_cell[i][0]-2][aro_uniq_cell[i][1]+2] == my_color:
			ok_cell_rep.append(aro_uniq_cell[i])
	if board[aro_uniq_cell[i][0]][aro_uniq_cell[i][1]+1] == opponent_color:
		if board [aro_uniq_cell[i][0]][aro_uniq_cell[i][1]+2] == my_color:
			ok_cell_rep.append(aro_uniq_cell[i])
	if board[aro_uniq_cell[i][0]+1][aro_uniq_cell[i][1]+1] == opponent_color:
		if board [aro_uniq_cell[i][0]+2][aro_uniq_cell[i][1]+2] == my_color:
			ok_cell_rep.append(aro_uniq_cell[i])

# print('置ける場所(重複削除してない)')
# print(ok_cell_rep)

# 2-2. ok_cell_repの重複を削除

ok_cell = []
for x in ok_cell_rep:
    if x not in ok_cell:
        ok_cell.append(x)
print('あなたの石の色：')
if my_color == 1:
	print('黒')
else:
	print('白')
print('置くことが可能なマス：')
print(ok_cell)

# 3. 石を置く

print('石を置く行を指定してください (例：2)')
# プレイヤーに入力させる
stone_row = input()

print('石を置く列を指定してください (例：3)')
# プレイヤーに入力させる
stone_col = input()


if [int(stone_row),int(stone_col)] in ok_cell:
	board[int(stone_row)][int(stone_col)] = my_color
	board_print.board_print(board) # 現時点での石の位置
else:
	print('ごめんなさい、そのマスには置けません。')


# 置ける場所がマークされてもいいよね


