#You are given two numbers a and b.
#Find the HCF and LCM of these two numbers
#and print them in a new line


A , B = map(int , input().split())
i = 1 
l = []
while i <= A:
    if A%i == 0 and B%i == 0:
        l.append(i)
    i += 1 
lcm = (A*B)//max(l)
print(max(l) , lcm)


#Sample Input 1:
#2 3

#Sample Output 1:
#1 6