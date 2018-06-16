
# Q. このファイルは何ですか？
# A. "board_print"関数が定義されているよ
#		正確に言えば… 本プログラムを実行すると、board_print関数を定義してくれるよ

# Q. board_print.pyとの違いは？
# A. board_print_wall.pyでは壁に対応しました(というか壁がある場合 専用)。

# Q. これ全部自分のプログラムにコピペすればいいんですか？
# A. それでもいいんだけど…面倒なので
#		1. 本プログラムを自分のプログラムと同じフォルダ内に保存する
#		2. 自分のプログラム内に以下を書いておく
#				import board_print_wall # = board_print_wall.pyを実行して、という意味
#		3. 関数を使いたいときは、以下のように
#				board_print_wall.board_print(...) # board_print_wall内のboard_print関数を使うよ、という意味
#	(詳しいことはよくわからないです、モジュール？)

# Q. board_print関数の具体的な使い方は？
# A. 	10 x 10 の 二次元配列(リストのリスト) を入力すると、boardをいい感じに表示する
#			壁を除いた 8x8部分のみを見る。各成分に対し、1なら黒丸、2なら白丸、3なら*(=置ける場所)、0なら空白 を表示。
#			ご自身の都合の良いように、変えていいです。

# ------------------------------------------------

def board_print(board):
    # 初期化：
	print_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

	for i in range(8):
		for j in range(8):
			if board[i+1][j+1]==2:
				print_board[i][j] = '○'
			elif board[i+1][j+1]==1:
				print_board[i][j] = '●'
			elif board[i+1][j+1]==3:
				print_board[i][j] = '*'
			elif board[i+1][j+1]==0:
				print_board[i][j] = ' '


	# print_boardを利用してオセロを表示
	print('  0 1 2 3 4 5 6 7 ')
	print(' +-+-+-+-+-+-+-+-+')
	for i in range(8):
		print(str(i), end="")
		for j in range(8):
			print('|'+print_board[i][j], end="")
		print('|')
	print(' +-+-+-+-+-+-+-+-+')
