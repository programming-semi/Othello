

def board_print(board):
    # 初期化：
	print_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

	for i in range(8):
		for j in range(8):
			if board[i][j]==2:
				print_board[i][j] = '○'
			elif board[i][j]==1:
				print_board[i][j] = '●'
			else:
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

