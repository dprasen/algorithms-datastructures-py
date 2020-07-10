def bubbleSort(arr):
    n = len(arr)

    #traversing through entire array
    for i in range(1,n):        
        for j in range(0,n-1):
            if( arr[j] < arr[j-1]):
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr                
