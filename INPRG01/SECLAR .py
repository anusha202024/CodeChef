#You are given three distinct integers A, B, and C.
#Find the 2′nd largest number among them and print it.


A = int(input())
B = int(input())
C = int(input())
if A>B and A>C:
	if B>C:
		print(B)
	else :
		print(C)
elif B>C:
	if C>A:
		print(C)
	else:
	    print(A)			
elif B>A:
	print(B)
else:
    print(A)


#Sample Input 2:
#14
#28
#16

#Sample Output 2:
#16
