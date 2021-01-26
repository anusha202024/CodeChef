#You are given a list of N integers 
#you need to reverse it and print the reversed list in a new line


N = int(input())
A = list(map(int , input().split()[:N]))
while N >= 1:
    N -= 1
    print(A[N] , end = " ")


#Sample Input 1:
#4
#1 3 2 4

#Sample Output 1:
#4 2 3 1