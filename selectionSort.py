def selectionSort(arr):
    arrayLength = len(arr)
    for outerIndex in range(arrayLength-1):
        min_index = outerIndex
        for innerIndex in range(outerIndex+1, arrayLength-1):
            if (arr[innerIndex] < arr[min_index]) : 
                min_index = innerIndex
                arr[outerIndex],arr[min_index] = arr[min_index],arr[outerIndex]
    return arr
