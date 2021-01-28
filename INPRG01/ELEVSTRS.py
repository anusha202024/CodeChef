T = int(input())
i = 1
while i<=T :
	N, V1, V2 = map(int, input().split())
	if 2*(V1**2) >= V2**2 :
		print("Stairs")
	else :
		print("Elevator")
	i = i+1