x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (4 <= x1 <= 32) and (4 <= y1 <= 32) and (4 <= x2 <= 32) and (4 <= y2 <= 32):
	if abs(x1-x2) + abs(y1-y2) <= 2:
		print('Yes')
	else:
		print('No')
else:
	print('Oshibka')
