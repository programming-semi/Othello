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
					n = n-1
					m = m+1
					
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
					
#ここからにひっくり返せる場所を探し、あればひっくり返す。
	if board[p-1][q] == opponent_color:
		k = p -1
		l = q
		while(board[k][l] == opponent_color): #見ている座標の位置を各方向ごとにずらしています
			k = k-1
			l = l
			if board[k][l] == my_color: #相手の色が続いた先に自分の色があったなら
				m = p-1
				n = q
				while( n <=k ): #mが自分の色があるマスまで(上のwhile文が終了したlまで)
					board[m][n] = my_color
					m = m-1
					n = n
		
