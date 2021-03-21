L , R = map(int , input().split())
while L <= R:
    if L%2==0:
        L += 1 
    else:
        print(L)
        L += 2