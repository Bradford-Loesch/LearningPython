def bubbleSort(arr):
    sort = False
    while (sort == False):
        sort = True
        for i in range (0, len(arr)-1):
            if (arr[i] > arr[i+1]):
                (arr[i], arr[i+1]) = (arr[i+1], arr[i])
                sort = False

def randomArr(length):
    import random
    arr = []
    for i in range (0, length):
        arr.append(random.randint(0,10000))
    return arr

testArray = randomArr(10000)
print testArray
bubbleSort(testArray)
print testArray
