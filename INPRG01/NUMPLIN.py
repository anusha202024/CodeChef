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
    