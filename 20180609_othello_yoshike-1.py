#初期状態
A= [[0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,2,1,0,0,0],
    [0,0,0,1,2,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]]

board=[]
#for a in A:				#Aの中の要素を1つずつ取り出す
#	board.append(a)			#boardという空リストにaを追加する
#	print (a)
#	print (board)
#石が置ける可能性のあるところを表示



B= [[0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]]
    

#成分全部0のBを作る理由：A内の2がおける成分をB内で2にするため
#具体例
#A= [[0,0,0,0,0,0,0,0],          B= [[0,0,0,0,0,0,0,0],]
#    [0,0,0,0,0,0,0,0],              [0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0],              [0,0,0,0,2,0,0,0],
#    [0,0,0,2,1,0,0,0],        →    [0,0,0,0,0,2,0,0],
#    [0,0,0,1,2,0,0,0],              [0,0,2,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0],              [0,0,0,2,0,0,0,0],
#    [0,0,0,0,0,0,0,0],              [0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0]]              [0,0,0,0,0,0,0,0],



#2がどこにおけるかを探す

for i in range(8):
	for j in range(8):
		if A[i][j]==2:  #まずは2を固定。ここが起点
#ここからは右をチェックするよ
			#if A[i][j+1]==1:   #2＝[i,j]成分の右が1じゃないと話は始まらないよってチェック
			k=1            #kは1から始めます。
			while A[i][j+k]==1:   #Aの[i,j+k]成分が1である限りｋを走らせる
				k=k+1             #kの走らせ方
			else:      #Aの[i,j+k]成分が1でないときは[while]文の操作が終わり、操作が終わったｋについて[else]以下が実行される
				if A[i][j+k]==0 and (k>=2):  #Aの[i,j+k]成分が0（空白）なら、Aの[i,j+k]成分には2がおけるよね
					B[i][j+k]=2   #Bの[i,j+k]成分に2を表示させる
					#if A[i][j+k]==壁
						#若林くん担当
						
#ここからは右下をチェックするよ
			if A[i+1][j+1]==1:   #2＝[i,j]成分の右下が1じゃないと話は始まらないよってチェック
				k=1
				while A[i+k][j+k]==1:
					k=k+1
				else:
					if A[i+k][j+k]==0:
						B[i+k][j+k]=2
					#if A[i+k][j+k]==壁
						#若林くん担当
						
#ここからは下をチェックするよ
			if A[i+1][j]==1:   #2＝[i,j]成分の下が1じゃないと話は始まらないよってチェック
				k=1
				while A[i+k][j]==1:
					k=k+1
				else:
					if A[i+k][j]==0:
						B[i+k][j]=2
					#if A[i+k][j]==壁
						#若林くん担当
				
#ここからは左下をチェックするよ
			if A[i+1][j-1]==1:   #2＝[i,j]成分の左下が1じゃないと話は始まらないよってチェック
				k=1
				while A[i+k][j-k]==1:
					k=k+1
				else:
					if A[i+k][j-k]==0:
						B[i+k][j-k]=2
					#if A[i+k][j-k]==壁
						#若林くん担当
						
#ここからは左をチェックするよ
			if A[i][j-1]==1:   #2＝[i,j]成分の左が1じゃないと話は始まらないよってチェック
				k=1
				while A[i][j-k]==1:
					k=k+1
				else:
					if A[i][j-k]==0:
						B[i][j-k]=2
					#if A[i][j-k]==壁
						#若林くん担当
						
#ここからは左上をチェックするよ
			if A[i-1][j-1]==1:   #2＝[i,j]成分の左上が1じゃないと話は始まらないよってチェック
				k=1
				while A[i-k][j-k]==1:
					k=k+1
				else:
					if A[i-k][j-k]==0:
						B[i-k][j-k]=2
					#if A[i-k][j-k]==壁
						#若林くん担当
						
#ここからは上をチェックするよ
			if A[i-1][j]==1:   #2＝[i,j]成分の上が1じゃないと話は始まらないよってチェック
				k=1
				while A[i-k][j]==1:
					k=k+1
				else:
					if A[i-k][j]==0:
						B[i-k][j]=2
					#if A[i-k][j]==壁
						#若林くん担当
						
#ここからは右上をチェックするよ
			if A[i-1][j+1]==1:   #2＝[i,j]成分の右上が1じゃないと話は始まらないよってチェック
				k=1
				while A[i-k][j+k]==1:
					k=k+1
				else:
					if A[i-k][j+k]==0:
						B[i-k][j+k]=2
					#if A[i-k][j+k]==壁
						#若林くん担当
for b in B:
	print(b)
		
		
		
