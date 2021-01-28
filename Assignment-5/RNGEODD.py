#You're given two numbers L and R.
#Print all odd numbers between L and R 
#(both inclusive) in a single line separated by space.
#And they should be in ascending order.

L , R = map(int , input().split())
while L <= R:
    if L%2==0:
        L += 1 
    else:
        print(L)
        L += 2

#Sample Input 1:
#2 9
#Sample Output 1:
#3 5 7 9
