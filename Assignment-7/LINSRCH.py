s = set()
for i in range(int(input())):
	s.add(int(input()))
print(1)
for j in range(int(input())):
	if int(input()) in s:
	    print("yes")
	else:
	    print("no")
