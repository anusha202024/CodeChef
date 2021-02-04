N = int(input())
for row in range(1 , N+1):
    for i in range(row , row*2 ):
        print(i , end = " ")
    for i in reversed(range(row , row*2-1 )):
        print(i , end = " ")
    print(" ")