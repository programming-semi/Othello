#��������E��ɂЂ�����Ԃ���ꏊ��T���A����΂Ђ�����Ԃ��B
	if board[p-1][q+1] == opponent_color:
		k = p -1
		l = q +1
		while(board[k][l] == opponent_color): #���Ă�����W�̈ʒu���e�������Ƃɂ��炵�Ă��܂�
			k = k-1
			l = l+1
			if board[k][l] == my_color: #����̐F����������Ɏ����̐F���������Ȃ�
				m = p-1
				n = q+1
				while( (m >=k) & (n <=l) ): #m�������̐F������}�X�܂�(���while�����I������l�܂�)
					board[m][n] = my_color
					n = n-1
					m = m+1
					
#��������E�ɂЂ�����Ԃ���ꏊ��T���A����΂Ђ�����Ԃ��B
	if board[p][q+1] == opponent_color:
		k = p
		l = q +1
		while(board[k][l] == opponent_color): #���Ă�����W�̈ʒu���e�������Ƃɂ��炵�Ă��܂�
			l = l+1
			if board[k][l] == my_color: #����̐F����������Ɏ����̐F���������Ȃ�
				n = q+1
				while( n <=l ): #m�������̐F������}�X�܂�(���while�����I������l�܂�)
					board[k][n] = my_color
					n = n+1
		
#��������E���ɂЂ�����Ԃ���ꏊ��T���A����΂Ђ�����Ԃ��B
	if board[p+1][q+1] == opponent_color:
		k = p +1
		l = q +1
		while(board[k][l] == opponent_color): #���Ă�����W�̈ʒu���e�������Ƃɂ��炵�Ă��܂�
			k = k+1
			l = l+1
			if board[k][l] == my_color: #����̐F����������Ɏ����̐F���������Ȃ�
				m = p+1
				n = q+1
				while( (m <=k) & (n <=l) ): #m�������̐F������}�X�܂�(���while�����I������l�܂�)
					board[m][n] = my_color
					n = n+1
					m = m+1

#�������獶��ɂЂ�����Ԃ���ꏊ��T���A����΂Ђ�����Ԃ��B
	if board[p-1][q-1] == opponent_color:
		k = p -1
		l = q -1
		while(board[k][l] == opponent_color): #���Ă�����W�̈ʒu���e�������Ƃɂ��炵�Ă��܂�
			k = k-1
			l = l-1
			if board[k][l] == my_color: #����̐F����������Ɏ����̐F���������Ȃ�
				m = p-1
				n = q-1
				while( (m >=k) & (n >=l) ): #m�������̐F������}�X�܂�(���while�����I������l�܂�)
					board[m][n] = my_color
					n = n-1
					m = m-1
					
#�������獶�ɂЂ�����Ԃ���ꏊ��T���A����΂Ђ�����Ԃ��B
	if board[p][q-1] == opponent_color:
		k = p
		l = q -1
		while(board[k][l] == opponent_color): #���Ă�����W�̈ʒu���e�������Ƃɂ��炵�Ă��܂�
			l = l-1
			if board[k][l] == my_color: #����̐F����������Ɏ����̐F���������Ȃ�
				n = q-1
				while( n >=l ): #m�������̐F������}�X�܂�(���while�����I������l�܂�)
					board[k][n] = my_color
					n = n-1
		
#�������獶���ɂЂ�����Ԃ���ꏊ��T���A����΂Ђ�����Ԃ��B
	if board[p+1][q-1] == opponent_color:
		k = p +1
		l = q -1
		while(board[k][l] == opponent_color): #���Ă�����W�̈ʒu���e�������Ƃɂ��炵�Ă��܂�
			k = k+1
			l = l-1
			if board[k][l] == my_color: #����̐F����������Ɏ����̐F���������Ȃ�
				m = p+1
				n = q-1
				while( (m <=k) & (n >=l) ): #m�������̐F������}�X�܂�(���while�����I������l�܂�)
					board[m][n] = my_color
					m = m+1
					n = n-1
					
#�������牺�ɂЂ�����Ԃ���ꏊ��T���A����΂Ђ�����Ԃ��B
	if board[p+1][q] == opponent_color:
		k = p +1
		l = q 
		while(board[k][l] == opponent_color): #���Ă�����W�̈ʒu���e�������Ƃɂ��炵�Ă��܂�
			k = k+1
			l = l
			if board[k][l] == my_color: #����̐F����������Ɏ����̐F���������Ȃ�
				m = p+1
				n = q
				while( m <=k ): #m�������̐F������}�X�܂�(���while�����I������l�܂�)
					board[m][n] = my_color
					m = m+1
					n = n
					
#��������ɂЂ�����Ԃ���ꏊ��T���A����΂Ђ�����Ԃ��B
	if board[p-1][q] == opponent_color:
		k = p -1
		l = q
		while(board[k][l] == opponent_color): #���Ă�����W�̈ʒu���e�������Ƃɂ��炵�Ă��܂�
			k = k-1
			l = l
			if board[k][l] == my_color: #����̐F����������Ɏ����̐F���������Ȃ�
				m = p-1
				n = q
				while( n <=k ): #m�������̐F������}�X�܂�(���while�����I������l�܂�)
					board[m][n] = my_color
					m = m-1
					n = n
		
