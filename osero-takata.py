#coding: utf=8

board = [[1,2,2,2,0,0,0,0],
		[2,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,2,1,0,0,0],
		[0,0,0,1,2,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]

my_color = 1
opponent_color = 3-my_color

for i in range(8):
	for j in range(8):
		if 0<i<7 and 0<j<7:
			if board[i][j] == opponent_color:
				if board[i-1][j-1] == 0:
					s = i
					k = j
					while s < 8 or k < 8:
						if board[s+1][k+1] == opponent_color:
							if s == 6 or k == 6:
								break
							else:
								s=s+1
								k=k+1
						elif board[s+1][k+1] == my_color:
							board[i-1][j-1] = 5
							break
						else:
							break

				if board[i-1][j] == 0:
					s = i
					k = j
					while s < 8:
						if board[s+1][k] == opponent_color:
							if s == 6:
								break
							else:
								s=s+1
						elif board[s+1][k] == my_color:
							board[i-1][j] = 5
							break
						else:
							break
					
				if board[i-1][j+1] == 0:
					s = i
					k = j
					while s < 8 and k >= 0:
						if board[s+1][k-1] == opponent_color:
							if s == 6 or k == 1:
								break
							else:
								s=s+1
								k=k-1
						elif board[s+1][k-1] == my_color:
							board[i-1][j+1] = 5
							break
						else:
							break
					
				if board[i][j-1] == 0:
					s = i
					k = j
					while k < 8:
						if board[s][k+1] == opponent_color:
							if k == 6:
								break
							else:
								k=k+1
						elif board[s][k+1] == my_color:
							board[i][j-1] = 5
							break
						else:
							break
					
				if board[i][j+1] == 0:
					s = i
					k = j
					while k >= 0:
						if board[s][k-1] == opponent_color:
							if k == 1:
								break
							else:
								k=k-1
						elif board[s][k-1] == my_color:
							board[i][j+1] = 5
							break
						else:
							break

				if board[i+1][j-1] == 0:
					s = i
					k = j
					while s >= 0 and k < 8:
						if board[s-1][k+1] == opponent_color:
							if s == 1 or k == 6:
								break
							else:
								s=s-1
								k=k+1
						elif board[s-1][k+1] == my_color:
							board[i+1][j-1] = 5
							break
						else:
							break

				if board[i+1][j] == 0:
					s = i
					k = j
					while s >= 0:
						if board[s-1][k] == opponent_color:
							if s == 1:
								break
							else:
								s=s-1
						elif board[s-1][k] == my_color:
							board[i+1][j] = 5
							break
						else:
							break

				if board[i+1][j+1] == 0:
					s = i
					k = j
					while s >= 0 and k >= 0:
						if board[s-1][k-1] == opponent_color:
							if s == 1 or k == 1:
								break
							else:
								s=s-1
								k=k-1
						elif board[s-1][k-1] == my_color:
							board[i+1][j+1] = 5
							break
						else:
							break
		elif (i == 0 or i == 7) and 0<j<7:
			if board[i][j] == opponent_color:
				if board[i][j-1] == 0:
					s = i
					k = j
					while k < 8:
						if board[s][k+1] == opponent_color:
							if k == 6:
								break
							else:
								k=k+1
						elif board[s][k+1] == my_color:
							board[i][j-1] = 5
							break
						else:
							break
					
				if board[i][j+1] == 0:
					s = i
					k = j
					while k >= 0:
						if board[s][k-1] == opponent_color:
							if k == 1:
								break
							else:
								k=k-1
						elif board[s][k-1] == my_color:
							board[i][j+1] = 5
							break
						else:
							break
		elif (j == 0 or j == 7) and 0<i<7:
			if board[i][j] == opponent_color:
				if board[i-1][j] == 0:
					s = i
					k = j
					while s < 8:
						if board[s+1][k] == opponent_color:
							if s == 6:
								break
							else:
								s=s+1
						elif board[s+1][k] == my_color:
							board[i-1][j] = 5
							break
						else:
							break

				if board[i+1][j] == 0:
					s = i
					k = j
					while s >= 0:
						if board[s-1][k] == opponent_color:
							if s == 1:
								break
							else:
								s=s-1
						elif board[s-1][k] == my_color:
							board[i+1][j] = 5
							break
						else:
							break

for a in board:
	print(a)

roop = 0
while roop<=0:
	print("石の配置場所を入力してください")

	num1 = int(input())
	num2 = int(input())

	if board[num1][num2] != 5:
		print("そこには置けないよ")

	elif board[num1][num2] == 5:
		board[num1][num2] = my_color
		if 1<num1<6 and 1<num2<6:
			if board[num1-1][num2-1] == opponent_color:
				s = num1-2
				k = num2-2
				while s>=0 and k>=0:
					if board[s][k] == opponent_color:
						s = s-1
						k = k-1
					elif board[s][k] == my_color:
						while s<8 and k<8:
							if board[s+1][k+1] == opponent_color:
								board[s+1][k+1] = my_color
								s=s+1
								k=k+1
							elif board[s+1][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1-1][num2] == opponent_color:
				s = num1-2
				k = num2
				while s>=0:
					if board[s][k] == opponent_color:
						s = s-1
					elif board[s][k] == my_color:
						while s<8:
							if board[s+1][k] == opponent_color:
								board[s+1][k] = my_color
								s=s+1
							elif board[s+1][k] == my_color:
								break
						break
					else:
						break

			if board[num1-1][num2+1] == opponent_color:
				s = num1-2
				k = num2+2
				while s>=0 and k<8:
					if board[s][k] == opponent_color:
						s = s-1
						k = k+1
					elif board[s][k] == my_color:
						while s<8 and k>=0:
							if board[s+1][k-1] == opponent_color:
								board[s+1][k-1] = my_color
								s=s+1
								k=k-1
							elif board[s+1][k-1] == my_color:
								break
						break
					else:
						break

			if board[num1][num2-1] == opponent_color:
				s = num1
				k = num2-2
				while k>=0:
					if board[s][k] == opponent_color:
						k = k-1
					elif board[s][k] == my_color:
						while k<8:
							if board[s][k+1] == opponent_color:
								board[s][k+1] = my_color
								k=k+1
							elif board[s][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1][num2+1] == opponent_color:
				s = num1
				k = num2+2
				while k<8:
					if board[s][k] == opponent_color:
						k = k+1
					elif board[s][k] == my_color:
						while k>=0:
							if board[s][k-1] == opponent_color:
								board[s][k-1] = my_color
								k=k-1
							elif board[s][k-1] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2-1] == opponent_color:
				s = num1+2
				k = num2-2
				while s<8 and k>=0:
					if board[s][k] == opponent_color:
						s = s+1
						k = k-1
					elif board[s][k] == my_color:
						while s>=0 and k<8:
							if board[s-1][k+1] == opponent_color:
								board[s-1][k+1] = my_color
								s=s-1
								k=k+1
							elif board[s-1][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2] == opponent_color:
				s = num1+2
				k = num2
				while s<8:
					if board[s][k] == opponent_color:
						s = s+1
					elif board[s][k] == my_color:
						while s>=0:
							if board[s-1][k] == opponent_color:
								board[s-1][k] = my_color
								s=s-1
							elif board[s-1][k] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2+1] == opponent_color:
				s = num1+2
				k = num2+2
				while s<8 and k<8:
					if board[s][k] == opponent_color:
						s = s+1
						k = k+1
					elif board[s][k] == my_color:
						while s>=0 and k>=0:
							if board[s-1][k-1] == opponent_color:
								board[s-1][k-1] = my_color
								s=s-1
								k=k-1
							elif board[s-1][k-1] == my_color:
								break
						break
					else:
						break
		elif (num1 == 1 and 1<num2<6) or (num1 == 0 and 1<num2<6):
			if board[num1][num2-1] == opponent_color:
				s = num1
				k = num2-2
				while k>=0:
					if board[s][k] == opponent_color:
						k = k-1
					elif board[s][k] == my_color:
						while k<8:
							if board[s][k+1] == opponent_color:
								board[s][k+1] = my_color
								k=k+1
							elif board[s][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1][num2+1] == opponent_color:
				s = num1
				k = num2+2
				while k<8:
					if board[s][k] == opponent_color:
						k = k+1
					elif board[s][k] == my_color:
						while k>=0:
							if board[s][k-1] == opponent_color:
								board[s][k-1] = my_color
								k=k-1
							elif board[s][k-1] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2-1] == opponent_color:
				s = num1+2
				k = num2-2
				while s<8 and k>=0:
					if board[s][k] == opponent_color:
						s = s+1
						k = k-1
					elif board[s][k] == my_color:
						while s>=0 and k<8:
							if board[s-1][k+1] == opponent_color:
								board[s-1][k+1] = my_color
								s=s-1
								k=k+1
							elif board[s-1][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2] == opponent_color:
				s = num1+2
				k = num2
				while s<8:
					if board[s][k] == opponent_color:
						s = s+1
					elif board[s][k] == my_color:
						while s>=0:
							if board[s-1][k] == opponent_color:
								board[s-1][k] = my_color
								s=s-1
							elif board[s-1][k] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2+1] == opponent_color:
				s = num1+2
				k = num2+2
				while s<8 and k<8:
					if board[s][k] == opponent_color:
						s = s+1
						k = k+1
					elif board[s][k] == my_color:
						while s>=0 and k>=0:
							if board[s-1][k-1] == opponent_color:
								board[s-1][k-1] = my_color
								s=s-1
								k=k-1
							elif board[s-1][k-1] == my_color:
								break
						break
					else:
						break
		elif (num1 == 6 and 1<num2<6) or (num1 == 7 and 1<num2<6):
			if board[num1-1][num2-1] == opponent_color:
				s = num1-2
				k = num2-2
				while s>=0 and k>=0:
					if board[s][k] == opponent_color:
						s = s-1
						k = k-1
					elif board[s][k] == my_color:
						while s<8 and k<8:
							if board[s+1][k+1] == opponent_color:
								board[s+1][k+1] = my_color
								s=s+1
								k=k+1
							elif board[s+1][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1-1][num2] == opponent_color:
				s = num1-2
				k = num2
				while s>=0:
					if board[s][k] == opponent_color:
						s = s-1
					elif board[s][k] == my_color:
						while s<8:
							if board[s+1][k] == opponent_color:
								board[s+1][k] = my_color
								s=s+1
							elif board[s+1][k] == my_color:
								break
						break
					else:
						break

			if board[num1-1][num2+1] == opponent_color:
				s = num1-2
				k = num2+2
				while s>=0 and k<8:
					if board[s][k] == opponent_color:
						s = s-1
						k = k+1
					elif board[s][k] == my_color:
						while s<8 and k>=0:
							if board[s+1][k-1] == opponent_color:
								board[s+1][k-1] = my_color
								s=s+1
								k=k-1
							elif board[s+1][k-1] == my_color:
								break
						break
					else:
						break

			if board[num1][num2-1] == opponent_color:
				s = num1
				k = num2-2
				while k>=0:
					if board[s][k] == opponent_color:
						k = k-1
					elif board[s][k] == my_color:
						while k<8:
							if board[s][k+1] == opponent_color:
								board[s][k+1] = my_color
								k=k+1
							elif board[s][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1][num2+1] == opponent_color:
				s = num1
				k = num2+2
				while k<8:
					if board[s][k] == opponent_color:
						k = k+1
					elif board[s][k] == my_color:
						while k>=0:
							if board[s][k-1] == opponent_color:
								board[s][k-1] = my_color
								k=k-1
							elif board[s][k-1] == my_color:
								break
						break
					else:
						break

		elif (num2 == 1 and 1<num1<6) or (num2 == 0 and 1<num1<6):
			if board[num1-1][num2] == opponent_color:
				s = num1-2
				k = num2
				while s>=0:
					if board[s][k] == opponent_color:
						s = s-1
					elif board[s][k] == my_color:
						while s<8:
							if board[s+1][k] == opponent_color:
								board[s+1][k] = my_color
								s=s+1
							elif board[s+1][k] == my_color:
								break
						break
					else:
						break

			if board[num1-1][num2+1] == opponent_color:
				s = num1-2
				k = num2+2
				while s>=0 and k<8:
					if board[s][k] == opponent_color:
						s = s-1
						k = k+1
					elif board[s][k] == my_color:
						while s<8 and k>=0:
							if board[s+1][k-1] == opponent_color:
								board[s+1][k-1] = my_color
								s=s+1
								k=k-1
							elif board[s+1][k-1] == my_color:
								break
						break
					else:
						break

			if board[num1][num2+1] == opponent_color:
				s = num1
				k = num2+2
				while k<8:
					if board[s][k] == opponent_color:
						k = k+1
					elif board[s][k] == my_color:
						while k>=0:
							if board[s][k-1] == opponent_color:
								board[s][k-1] = my_color
								k=k-1
							elif board[s][k-1] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2] == opponent_color:
				s = num1+2
				k = num2
				while s<8:
					if board[s][k] == opponent_color:
						s = s+1
					elif board[s][k] == my_color:
						while s>=0:
							if board[s-1][k] == opponent_color:
								board[s-1][k] = my_color
								s=s-1
							elif board[s-1][k] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2+1] == opponent_color:
				s = num1+2
				k = num2+2
				while s<8 and k<8:
					if board[s][k] == opponent_color:
						s = s+1
						k = k+1
					elif board[s][k] == my_color:
						while s>=0 and k>=0:
							if board[s-1][k-1] == opponent_color:
								board[s-1][k-1] = my_color
								s=s-1
								k=k-1
							elif board[s-1][k-1] == my_color:
								break
						break
					else:
						break

		elif (num2 == 6 and 1<num1<6) or (num2 == 7 and 1<num1<6):
			if board[num1-1][num2-1] == opponent_color:
				s = num1-2
				k = num2-2
				while s>=0 and k>=0:
					if board[s][k] == opponent_color:
						s = s-1
						k = k-1
					elif board[s][k] == my_color:
						while s<8 and k<8:
							if board[s+1][k+1] == opponent_color:
								board[s+1][k+1] = my_color
								s=s+1
								k=k+1
							elif board[s+1][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1-1][num2] == opponent_color:
				s = num1-2
				k = num2
				while s>=0:
					if board[s][k] == opponent_color:
						s = s-1
					elif board[s][k] == my_color:
						while s<8:
							if board[s+1][k] == opponent_color:
								board[s+1][k] = my_color
								s=s+1
							elif board[s+1][k] == my_color:
								break
						break
					else:
						break

			if board[num1][num2-1] == opponent_color:
				s = num1
				k = num2-2
				while k>=0:
					if board[s][k] == opponent_color:
						k = k-1
					elif board[s][k] == my_color:
						while k<8:
							if board[s][k+1] == opponent_color:
								board[s][k+1] = my_color
								k=k+1
							elif board[s][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2-1] == opponent_color:
				s = num1+2
				k = num2-2
				while s<8 and k>=0:
					if board[s][k] == opponent_color:
						s = s+1
						k = k-1
					elif board[s][k] == my_color:
						while s>=0 and k<8:
							if board[s-1][k+1] == opponent_color:
								board[s-1][k+1] = my_color
								s=s-1
								k=k+1
							elif board[s-1][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2] == opponent_color:
				s = num1+2
				k = num2
				while s<8:
					if board[s][k] == opponent_color:
						s = s+1
					elif board[s][k] == my_color:
						while s>=0:
							if board[s-1][k] == opponent_color:
								board[s-1][k] = my_color
								s=s-1
							elif board[s-1][k] == my_color:
								break
						break
					else:
						break

		elif 0<=num1<=1 and 0<=num2<=1:
			if board[num1][num2+1] == opponent_color:
				s = num1
				k = num2+2
				while k<8:
					if board[s][k] == opponent_color:
						k = k+1
					elif board[s][k] == my_color:
						while k>=0:
							if board[s][k-1] == opponent_color:
								board[s][k-1] = my_color
								k=k-1
							elif board[s][k-1] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2] == opponent_color:
				s = num1+2
				k = num2
				while s<8:
					if board[s][k] == opponent_color:
						s = s+1
					elif board[s][k] == my_color:
						while s>=0:
							if board[s-1][k] == opponent_color:
								board[s-1][k] = my_color
								s=s-1
							elif board[s-1][k] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2+1] == opponent_color:
				s = num1+2
				k = num2+2
				while s<8 and k<8:
					if board[s][k] == opponent_color:
						s = s+1
						k = k+1
					elif board[s][k] == my_color:
						while s>=0 and k>=0:
							if board[s-1][k-1] == opponent_color:
								board[s-1][k-1] = my_color
								s=s-1
								k=k-1
							elif board[s-1][k-1] == my_color:
								break
						break
					else:
						break

		elif 0<=num1<=1 and 6<=num2<=7:
			if board[num1+1][num2-1] == opponent_color:
				s = num1+2
				k = num2-2
				while s<8 and k>=0:
					if board[s][k] == opponent_color:
						s = s+1
						k = k-1
					elif board[s][k] == my_color:
						while s>=0 and k<8:
							if board[s-1][k+1] == opponent_color:
								board[s-1][k+1] = my_color
								s=s-1
								k=k+1
							elif board[s-1][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1+1][num2] == opponent_color:
				s = num1+2
				k = num2
				while s<8:
					if board[s][k] == opponent_color:
						s = s+1
					elif board[s][k] == my_color:
						while s>=0:
							if board[s-1][k] == opponent_color:
								board[s-1][k] = my_color
								s=s-1
							elif board[s-1][k] == my_color:
								break
						break
					else:
						break

			if board[num1][num2-1] == opponent_color:
				s = num1
				k = num2-2
				while k>=0:
					if board[s][k] == opponent_color:
						k = k-1
					elif board[s][k] == my_color:
						while k<8:
							if board[s][k+1] == opponent_color:
								board[s][k+1] = my_color
								k=k+1
							elif board[s][k+1] == my_color:
								break
						break
					else:
						break

		elif 6<=num1<=7 and 0<=num2<=1:
			if board[num1-1][num2] == opponent_color:
				s = num1-2
				k = num2
				while s>=0:
					if board[s][k] == opponent_color:
						s = s-1
					elif board[s][k] == my_color:
						while s<8:
							if board[s+1][k] == opponent_color:
								board[s+1][k] = my_color
								s=s+1
							elif board[s+1][k] == my_color:
								break
						break
					else:
						break

			if board[num1-1][num2+1] == opponent_color:
				s = num1-2
				k = num2+2
				while s>=0 and k<8:
					if board[s][k] == opponent_color:
						s = s-1
						k = k+1
					elif board[s][k] == my_color:
						while s<8 and k>=0:
							if board[s+1][k-1] == opponent_color:
								board[s+1][k-1] = my_color
								s=s+1
								k=k-1
							elif board[s+1][k-1] == my_color:
								break
						break
					else:
						break

			if board[num1][num2+1] == opponent_color:
				s = num1
				k = num2+2
				while k<8:
					if board[s][k] == opponent_color:
						k = k+1
					elif board[s][k] == my_color:
						while k>=0:
							if board[s][k-1] == opponent_color:
								board[s][k-1] = my_color
								k=k-1
							elif board[s][k-1] == my_color:
								break
						break
					else:
						break

		elif 6<=num1<=7 and 6<=num2<=7:
			if board[num1-1][num2-1] == opponent_color:
				s = num1-2
				k = num2-2
				while s>=0 and k>=0:
					if board[s][k] == opponent_color:
						s = s-1
						k = k-1
					elif board[s][k] == my_color:
						while s<8 and k<8:
							if board[s+1][k+1] == opponent_color:
								board[s+1][k+1] = my_color
								s=s+1
								k=k+1
							elif board[s+1][k+1] == my_color:
								break
						break
					else:
						break

			if board[num1-1][num2] == opponent_color:
				s = num1-2
				k = num2
				while s>=0:
					if board[s][k] == opponent_color:
						s = s-1
					elif board[s][k] == my_color:
						while s<8:
							if board[s+1][k] == opponent_color:
								board[s+1][k] = my_color
								s=s+1
							elif board[s+1][k] == my_color:
								break
						break
					else:
						break

			if board[num1][num2-1] == opponent_color:
				s = num1
				k = num2-2
				while k>=0:
					if board[s][k] == opponent_color:
						k = k-1
					elif board[s][k] == my_color:
						while k<8:
							if board[s][k+1] == opponent_color:
								board[s][k+1] = my_color
								k=k+1
							elif board[s][k+1] == my_color:
								break
						break
					else:
						break
		roop = 1

for a in board:
	print(a)
