def replace(arr):

    while len(arr) > 1:
        arr.sort()

        min1 = arr[0]
        min2 = arr[1]
        counter = 2
        while min2 == min1 and counter < n:
            min2 = arr[counter]
            counter += 1
        newValue = (3*min1+2*min2) % 100
        arr.remove(min1)
        arr.remove(min2)
        arr.insert(0, newValue)
    print(arr[0])


arr = []
for i in range(int(input())):
        arr.append(int(input()))
replace(arr)