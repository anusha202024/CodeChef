N = int(input())
A = list(map(int , input().split()[:N]))
while N >= 1:
    N -= 1
    print(A[N] , end = " ")

