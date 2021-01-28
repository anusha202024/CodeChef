#You are given two integers A and B. 
#Print the number closest to A but less than or equal to A which is completely divisible by B.

A = int(input())
B = int(input())
if A<B :
	print("0")
else :
	print( (A//B)*B )
	
	
#Sample Input 1:
#23
#7
#Sample Output 1:
#21
