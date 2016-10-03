def randomArr(length):
    import random
    arr = []
    for i in range (0, length):
        arr.append(random.randint(0,10000))
    return arr

testArray = randomArr(100000)
# print "Unsorted:", testArray

def selectionSort(arr):
    for i in range (0,len(arr)):
        min = arr[i];
        mini = i
        for j in range (i+1, len(arr)):
            if(arr[j] < min):
                min = arr[j]
                mini = j
        (arr[i], arr[mini]) = (arr[mini], arr[i])
    return arr

# MinMax selection sorting method
def selectionSortMM(arr):
    maxcount = 0
    endpos = len(arr)-1
    for i in range (0,len(arr)/2):
        min = arr[i]
        mini = i
        max = arr[i]
        maxi = i
        for j in range (i+1, endpos+1):
            if(arr[j] < min):
                min = arr[j]
                mini = j
            if(arr[j] > max):
                max = arr[j]
                maxi = j
        (arr[i], arr[mini]) = (arr[mini], arr[i])
        (arr[maxi], arr[endpos]) = (arr[endpos], arr[maxi])
        endpos -= 1
    return arr

import time
start = time.time()
print "Min sort:", selectionSort(testArray)
end = time.time()
print (end - start)
start = time.time()

print "Min and max sort:", selectionSortMM(testArray)
end = time.time()
print (end - start)
