def insertionSort(arr):
    n = len(arr)
    for index in range(n):
        currentVal = arr[index]
        currentPos = index

        while currentPos > 0 and arr[currentPos - 1] > currentVal:            
            arr[currentPos] = arr[currentPos -1]
            currentPos = currentPos - 1
        
        arr[currentPos] = currentVal

    return arr            


