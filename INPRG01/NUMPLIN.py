#You're given a number N, now check if the number N is palindrome or not.
#Print "YES"(without quotes) if it's a palindrome, otherwise print "NO" (without quotes).


N = int(input())
original_N = N
result = 0 
while N != 0:
    r = N%10
    result = 10*result + r
    N = N//10
if result == original_N:
    print("YES")
else:
    print("NO")
    
    
#Sample Input 1:
#8668
#Sample Output 1:
#YES
    
