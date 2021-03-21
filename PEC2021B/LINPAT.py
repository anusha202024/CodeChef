N = int(input())
i , j , l = 1 , 0 , []
while i <= N and i > 0:
	o = 10*i
	e = 2*i
	l.append(o)
	l.append(e)
	i = i + 1
	print(l[j] , end = " ")
	j = j + 1