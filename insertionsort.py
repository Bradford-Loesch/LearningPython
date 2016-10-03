def randomArr(length):
    import random
    arr = []
    for i in range (0, length):
        arr.append(random.randint(0,10000))
    return arr

testArray = randomArr(10000)

def insertionSort(arr):
    if (arr[0] > arr[1]):
        (arr[0], arr[1]) = (arr[1], arr[0])
    for i in range(2,len(arr)):
        for j in range(i-1,-1,-1):
            if (j > 0):
                if (arr[i] < arr[j] and arr[i] > arr[j-1]):
                    temp = arr[i]
                    del arr[i]
                    arr.insert(j,temp)
            else:
                if (arr[i] < arr[j]):
                    temp = arr[i]
                    del arr[i]
                    arr.insert(j,temp)
    return arr

print insertionSort(testArray)
