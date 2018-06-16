
di = list(itertools.product([-1,0,1], [-1,0,1])) # 8方向を表すリスト
# di = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

for i in range(8): # 各行の
	for j in range(8): # 各列の(つまり各マスの)
		for l in range(len(di)): # 各方向(8つ)に対して
			if board[i+1][j+1] == my_color: # 自分の石があるマスならば以下を実行：
				if board[(i+1)+di[l][0]*1][(j+1)+di[l][1]*1]==opponent_color: # 相手の色が隣にある場合
					k=1
					while board[(i+1)+di[l][0]*k][(j+1)+di[l][1]*k]==opponent_color: # 相手の色が隣に続く限りループ
						k=k+1
					else: # ループ抜けたら
						if board[(i+1)+di[l][0]*k][(j+1)+di[l][1]*k]==0: # その先が空白ならば
							board[(i+1)+di[l][0]*k][(j+1)+di[l][1]*k]=3 # 石を置けるよ

