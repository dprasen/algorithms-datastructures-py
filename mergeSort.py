def mergeSort(arr):
    arrayLength = len(arr)
    if arrayLength > 1:
        midOfArray = arrayLength // 2
        leftPart = arr[:midOfArray]
        rightPart = arr[midOfArray:]

        mergeSort(leftPart)
        mergeSort(rightPart)

        i=j=k=0 #initialise counter

        while i < len(leftPart) and j < len(rightPart):
            if leftPart[i] < rightPart[j]:
                arr[k] = leftPart[i]
                i=i+1
                k=k+1
            else:
                arr[k] = rightPart[j]
                j=j+1
                k=k+1
        
        while i < len(leftPart):
            arr[k] = leftPart[i]
            i=i+1
            k=k+1
        
        while j < len(rightPart):
            arr[k] = rightPart[j]
            j=j+1
            k=k+1
    
    return arr