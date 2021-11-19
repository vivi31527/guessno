import random
start = input('請決定隨機數字範圍最小值(min):')
end = input('請決定隨機數字範圍最大值(max):')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	num = input('請猜一個數字:')
	num = int(num)
	count += 1
	if num == r:
		print('這是你猜的第', count, '次, 恭喜你猜對了!')
		break
	elif num > r:
		print('猜錯了~答案是更小的數字!')
	elif num < r:
		print('猜錯了~答案是更大的數字!')
	print('這是你猜的第', count, '次')