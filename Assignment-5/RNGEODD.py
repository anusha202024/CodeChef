#You're given two numbers L and R.
#Print all odd numbers between L and R 
#(both inclusive) in a single line separated by space.
#And they should be in ascending order.

N , K = map(int , input().split())
A = list(map(int, input().split()[:N]))
if K in A:
    print(1)
else:
    print(-1)

#Sample Input 1:
#2 9
#Sample Output 1:
#3 5 7 9
