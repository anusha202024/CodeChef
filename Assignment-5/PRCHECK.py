#You are given a number N
#check if this number is a prime pr not.
#If this number is prime the print 1,
#otherwise print 0.

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


#Sample Input 1:
#6

#Sample Output 1:
#0