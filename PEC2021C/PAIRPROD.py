n = int(input())
sum = int(input())
tsum = 0

for i in range(n-1):
	num = int(input())
	tsum += num*sum
	sum += num

print(2)
print(tsum)