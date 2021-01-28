#Given a number N and check if its second last digit is 7 or not.
#If it's 7 then print 1, otherwise print 0 in a single line


N = int(input())
if (N//10)%10 == 7:
	print(1) 
else:
	print(0)
	
	
#Sample Input 2:
#4176
#Sample Output 2:
#1
