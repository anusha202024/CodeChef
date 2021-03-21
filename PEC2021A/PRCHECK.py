N = int(input())
count = 0
i = 1
while i**2 <= N:
	if N%i == 0 :
		count += 1
	i += 1
if count == 1 and N!= 1 :
	print(1)
else :
	print(0)