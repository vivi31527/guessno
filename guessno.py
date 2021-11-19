import random

r = random.randint(1, 100)
count = 0
while True:
	num = input('請猜一個數字:')
	num = int(num)
	if num == r:
		print('恭喜你猜對了')
		break
	elif num > r:
		print('猜錯了~答案是更小的數字!')
	elif num < r:
		print('猜錯了~答案是更大的數字!')
	count += 1
	print('這是你猜的第', count, '次')