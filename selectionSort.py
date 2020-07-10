def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n-1):
            if (arr[j] < arr[min_index]) : 
                min_index = j
                arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
