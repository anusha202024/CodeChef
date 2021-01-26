#You are given a list of N integers and a value K.
#print 1 if K exists in the given list of N integers,
#otherwise print −1.


N , K = map(int , input().split())
A = list(map(int, input().split()[:N]))
if K in A:
    print(1)
else:
    print(-1)


#Sample Input 1:
#4 2
#1 2 3 4

#Sample Output 1:
#1