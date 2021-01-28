#Odd Even Multiple 

#You are given an integer N. If N is not divisible by 3 then print −1.
#If N is an odd multiple of 3 the print 1
#and if N is an even multiple of 3 then print 0.

N =int(input())
if N%3 != 0:
    print("-1")
elif N%6 == 0:
    print("0")
else:
    print("1")
    
#Sample Input 1:
#24
#Sample Output 1:
#0
