
# できてから、より効率の良い方法を考える

# ----------------------------------------

# -- board --

# 色情報の入った8x8の行列 で再現すれば、なんとかなりそう
# 色情報が、操作によってどんどん更新されていく

# 色：整数で表現
#	別に"kuro"とか"shiro"でもいいんだろうけど、利便性を考えて
# 1 : 黒, 2 : 白, -1:壁(wall), 0 : 何もいない

# 行列：リスト(ベクトルみたいなやつ、中にデータを入れられる) を使う
#	リストの中にリストを入れることで、「行列」のようなものが再現可能
# 	某Deep learningの本曰く、Numpy?というモジュールが便利らしい
# list=[1,2,3,4,5]のように定義, list[0]とやると、1番目が取り出せる

# とりあえず、初期boardの生成
#board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,0,0,2,1,0,0,0,-1],[-1,0,0,0,1,2,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

# 画像1をboardに反映させる
#board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,2,0,0,0,0,0,0,-1],[-1,0,0,2,0,0,1,0,0,-1],[-1,0,0,0,2,1,1,0,0,-1],[-1,0,0,0,2,2,1,0,0,-1],[-1,0,0,0,2,0,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

# 画像2をboardに反映させる
#board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,0,1,0,0,0,0,0,-1],[-1,0,0,0,1,1,2,0,0,-1],[-1,0,0,0,2,2,1,0,0,-1],[-1,0,0,0,2,0,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,0,0,0,0,0,0,0,0,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

# 画像3をboardに反映させる
#board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,0,0,0,1,1,1,1,1,-1],[-1,1,0,1,1,1,1,1,2,-1],[-1,0,1,0,0,1,2,1,2,-1],[-1,0,0,1,1,2,2,1,1,-1],[-1,0,0,1,2,2,2,1,1,-1],[-1,0,0,2,0,2,2,2,2,-1],[-1,0,2,0,0,0,2,2,2,-1],[-1,2,0,0,0,0,2,1,1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

# めっちゃ白
board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,1,1,1,1,1,1,1,1,-1],[-1,1,2,2,2,2,2,2,1,-1],[-1,1,2,2,2,2,2,2,1,-1],[-1,1,2,2,2,2,2,2,1,-1],[-1,1,2,2,0,2,2,2,1,-1],[-1,1,2,2,2,2,2,2,1,-1],[-1,1,2,2,2,2,2,2,1,-1],[-1,1,1,1,1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]



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
# board_print.board_print(board) # 現在のboardを表示してくれるよ
	# 厳密に言うと10x10行列を与えると、各要素に対して、1ならば●、2ならば○、4ならば！、どちらでもないならば" "を、いい感じにデザインして表示

# ----------------------------------------


# -- 置ける場所をチェックする --

# 今の石状況を見て、置けるマスの行と列を返す

# --

# 0. 相手の色の定義(この位置でいいかはちょっと考える)
opponent_color = 3-my_color


# 1. 隣に相手の色があり、かつ、まだ何もないマスを抽出する(赤フローチャートの最初の分岐をクリアするもの)

# 1-1. 相手の色のマスを全て抽出

my_cell = [] # 他の色があるマス
for i in range(10): 
	for j in range(10):
		if board[i][j] == my_color: #自分の色の石がある座標を選別しています
			my_cell.append([i,j]) #"自分の石の色がある座標の集合"の作成
#print('自分の色があるマス：')
#print(my_cell)

ok_cell_rep = [] #"置ける座標の集合"の作成
for i in range(len(my_cell)):
	i_0 = my_cell[i][0]
	j_0 = my_cell[i][1]
#ここから右をチェックします
	if board[i_0][j_0 +1] == opponent_color:
		k = i_0
		l = j_0 +1
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			l = l+1
		else:
			if board[k][l] == 0:
				ok_cell_rep.append([k,l]) #置ける石の位置の座標を"置ける集合"に入れてあげます
				board[k][l] = 4           #画面上に置ける石の位置を表示するために値を変更しています(値が 4 である理由は特にありません)
#ここから左をチェックします
	if board[i_0][j_0 -1] == opponent_color:
		k = i_0
		l = j_0 - 1
		while(board[k][l] == opponent_color):
			l = l-1
		else:
			if board[k][l] == 0:
				ok_cell_rep.append([k,l])
				board[k][l] = 4

#ここから上をチェックします
	if board[i_0 -1][j_0] == opponent_color:
		k = i_0 -1
		l = j_0
		while(board[k][l] == opponent_color):
			k = k-1
		else:
			if board[k][l] == 0:
				ok_cell_rep.append([k,l])
				board[k][l] = 4

#ここから下をチェックします
	if board[i_0 +1][j_0] == opponent_color:
		k = i_0 +1
		l = j_0
		while(board[k][l] == opponent_color):
			k = k+1
		else:
			if board[k][l] == 0:
				ok_cell_rep.append([k,l])
				board[k][l] = 4

#ここから右上をチェックします
	if board[i_0 -1][j_0 +1] == opponent_color:
		k = i_0 -1
		l = j_0 +1
		while(board[k][l] == opponent_color):
			k = k-1
			l = l+1
		else:
			if board[k][l] == 0:
				ok_cell_rep.append([k,l])
				board[k][l] = 4

#ここから右下をチェックします
	if board[i_0 +1][j_0 +1] == opponent_color:
		k = i_0 +1
		l = j_0 + 1
		while(board[k][l] == opponent_color):
			k = k+1
			l = l+1
		else:
			if board[k][l] == 0:
				ok_cell_rep.append([k,l])
				board[k][l] = 4

#ここから左上をチェックします
	if board[i_0 -1][j_0 -1] == opponent_color:
		k = i_0 -1
		l = j_0 -1
		while(board[k][l] == opponent_color):
			k = k-1
			l = l-1
		else:
			if board[k][l] == 0:
				ok_cell_rep.append([k,l])
				board[k][l] = 4

#ここから左下をチェックします
	if board[i_0 +1][j_0 -1] == opponent_color:
		k = i_0 +1
		l = j_0 -1
		while(board[k][l] == opponent_color):
			k = k+1
			l = l-1
		else:
			if board[k][l] == 0:
				ok_cell_rep.append([k,l])
				board[k][l] = 4

board_print.board_print(board)

# print('置ける場所(重複削除してない)')
# print(ok_cell_rep)

# 2-2. ok_cell_repの重複を削除

ok_cell = []
for x in ok_cell_rep:
    if x not in ok_cell:
        ok_cell.append(x)
print('あなたの石の色')
if my_color ==1:
	print('黒')
else:
	print('白')

print('置くことが可能なマス：')
print(ok_cell_rep)
print('石を置く行を指定してください (例：2)')
# プレイヤーに入力させる
stone_row = input()

print('石を置く列を指定してください (例：3)')
# プレイヤーに入力させる
stone_col = input()

p = int(stone_row)
q = int(stone_col)
if [p,q] in ok_cell:
	board[int(stone_row)][int(stone_col)] = my_color
	for x in ok_cell:
		if board[x[0]][x[1]] == 4:
			board[x[0]][x[1]] = 0          #置ける石の位置の"！"を削除
			
#ここから右上にひっくり返せる場所を探し、あればひっくり返す。
	if board[p-1][q+1] == opponent_color:
		k = p -1
		l = q +1
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			k = k-1
			l = l+1
			if board[k][l] == my_color: #相手の色が続いた先に自分の色があったなら
				m = p-1
				n = q+1
				while( (m >=k) & (n <=l) ): #mが自分の色があるマスまで(上のwhile文が終了したlまで)
					board[m][n] = my_color
					m = m-1
					n = n+1
					
#ここから右にひっくり返せる場所を探し、あればひっくり返す。
	if board[p][q+1] == opponent_color:
		k = p
		l = q +1
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			l = l+1
			if board[k][l] == my_color: #相手の色が続いた先に自分の色があったなら
				n = q+1
				while( n <=l ): #mが自分の色があるマスまで(上のwhile文が終了したlまで)
					board[k][n] = my_color
					n = n+1
		
#ここから右下にひっくり返せる場所を探し、あればひっくり返す。
	if board[p+1][q+1] == opponent_color:
		k = p +1
		l = q +1
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			k = k+1
			l = l+1
			if board[k][l] == my_color: #相手の色が続いた先に自分の色があったなら
				m = p+1
				n = q+1
				while( (m <=k) & (n <=l) ): #mが自分の色があるマスまで(上のwhile文が終了したlまで)
					board[m][n] = my_color
					n = n+1
					m = m+1

#ここから左上にひっくり返せる場所を探し、あればひっくり返す。
	if board[p-1][q-1] == opponent_color:
		k = p -1
		l = q -1
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			k = k-1
			l = l-1
			if board[k][l] == my_color: #相手の色が続いた先に自分の色があったなら
				m = p-1
				n = q-1
				while( (m >=k) & (n >=l) ): #mが自分の色があるマスまで(上のwhile文が終了したlまで)
					board[m][n] = my_color
					n = n-1
					m = m-1
					
#ここから左にひっくり返せる場所を探し、あればひっくり返す。
	if board[p][q-1] == opponent_color:
		k = p
		l = q -1
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			l = l-1
			if board[k][l] == my_color: #相手の色が続いた先に自分の色があったなら
				n = q-1
				while( n >=l ): #mが自分の色があるマスまで(上のwhile文が終了したlまで)
					board[k][n] = my_color
					n = n-1
		
#ここから左下にひっくり返せる場所を探し、あればひっくり返す。
	if board[p+1][q-1] == opponent_color:
		k = p +1
		l = q -1
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			k = k+1
			l = l-1
			if board[k][l] == my_color: #相手の色が続いた先に自分の色があったなら
				m = p+1
				n = q-1
				while( (m <=k) & (n >=l) ): #mが自分の色があるマスまで(上のwhile文が終了したlまで)
					board[m][n] = my_color
					m = m+1
					n = n-1
		
#ここから下にひっくり返せる場所を探し、あればひっくり返す。
	if board[p+1][q] == opponent_color:
		k = p +1
		l = q 
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			k = k+1
			l = l
			if board[k][l] == my_color: #相手の色が続いた先に自分の色があったなら
				m = p+1
				n = q
				while( m <=k ): #mが自分の色があるマスまで(上のwhile文が終了したlまで)
					board[m][n] = my_color
					m = m+1
					n = n
					
#ここから上にひっくり返せる場所を探し、あればひっくり返す。
	if board[p-1][q] == opponent_color:
		k = p -1
		l = q
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			k = k-1
			l = l
			if board[k][l] == my_color: #相手の色が続いた先に自分の色があったなら
				m = p-1
				n = q
				while( m >=k ): #mが自分の色があるマスまで(上のwhile文が終了したlまで)
					board[m][n] = my_color
					m = m-1
					n = n
					
					
	board_print.board_print(board) # 現時点での石の位置
	
else:
	print('ごめんなさい、そのマスには置けません。')
	


