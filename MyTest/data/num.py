while True:
	txt = input('input:')
	if txt == 'stop':
		break
	elif not txt.isdigit():#isdigit()方法用于判断是否为数字
		print("你输入的不是数字！！")
	else:
		num = int(txt)
		if num < 20:
			print("太小了")
		elif num > 20:
			print("太大了")
		else:
			print("猜对了")
