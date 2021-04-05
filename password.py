x = 3
		
while x > 0:
	password = input('請輸入密碼: ')
	if password == '12345':
		print('成功登錄')
		break
	elif password != '12345':
		x = x - 1
		print('還有', x, '次機會')
while x <= 0:
	print('你不要亂玩~~~~')
	break

