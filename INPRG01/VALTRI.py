#Raju is planning to visit his favorite restaurant and travels to it by bus.
#Only the buses whose numbers are divisible by 5 or by 6 will take him to his destination.
#Now you are given bus number N and find if Raju can take the bus or not.
#Print "YES"(without quotes) if he can take the bus, otherwise print "NO" (without quotes).


N = int(input())
if N%5 == 0 or N%6 ==0:
    print("YES")
else:
    print("NO")

    
#Sample Input 1:
#0
#Sample Output 1:
#YES
