A , B = map(int , input().split())
i = 1 
l = []
while i <= A:
    if A%i == 0 and B%i == 0:
        l.append(i)
    i += 1 
lcm = (A*B)//max(l)
print(max(l) , lcm)