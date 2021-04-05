x = 3
password = '12345'

while x > 0:
	x = x - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('成功登錄')
		break
	else:
		if x >0:
			print('還有', x, '次機會')
		if x <= 0:
			print('你不要亂玩~~~~')
			break
