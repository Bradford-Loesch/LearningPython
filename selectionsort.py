def randomArr(length):
    import random
    arr = []
    for i in range (0, length):
        arr.append(random.randint(0,100))
    return arr

testArray = randomArr(10)
print "Unsorted:", testArray

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
    arr =  [62, 22, 64, 51, 10, 48, 36, 4, 41, 59]
    maxcount = 0
    end = len(arr)-1
    for i in range (0,len(arr)/2):
        min = arr[i]
        mini = i
        max = arr[i]
        maxi = i
        for j in range (i+1, len(arr)-i):
            if(arr[j] < min):
                min = arr[j]
                mini = j
            if(arr[j] > max):
                max = arr[j]
                maxi = j
        end = len(arr)-i-1
        print arr, i, mini, len(arr)-i-1, maxi
        if (mini == len(arr)-i-1 and maxi == i):
            (arr[i], arr[mini]) = (arr[mini], arr[i])
        elif (maxi == i):
            (arr[maxi], arr[end]) = (arr[end], arr[maxi])
            (arr[i], arr[mini]) = (arr[mini], arr[i])
        else:
            (arr[i], arr[mini]) = (arr[mini], arr[i])
            (arr[maxi], arr[end]) = (arr[end], arr[maxi])
    return arr

import time
# start = time.time()
# print "Min sort:", selectionSort(testArray)
# end = time.time()
# print (end - start)

start = time.time()
print "Min and max sort:", selectionSortMM(testArray)
end = time.time()
print (end - start)
