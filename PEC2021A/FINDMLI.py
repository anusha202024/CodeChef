N , K = map(int , input().split())
A = list(map(int, input().split()[:N]))
if K in A:
    print(1)
else:
    print(-1)