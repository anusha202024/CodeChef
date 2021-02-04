N = int(input())
for row in range( 1 , N+1):
	if row%2 == 0:
		for i in reversed(range(row*5 - 4 , row*5 + 1)):
			print(i , end = " ")
		print(" ")
	else:
		for i in range(row*5 - 4, row*5+1):
			print(i , end = " ")
		print(" ")