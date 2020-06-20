#最大公倍数
def lcm(x,y):
	greater = x if x > y else y
	while (True):
		if (greater % x == 0) and (greater % y == 0):
			return greater
		else:
			greater += 1

if __name__ == '__main__':
	x = 5
	y = 7

	print(lcm(x,y))

