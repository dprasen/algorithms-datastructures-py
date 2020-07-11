def heapUp(arr,n,i):
    largest = i     # largest value
    l = 2 * i + 1    #leftnode
    r = 2 * i + 2    #rightnode
    # if left child exists
    if l < n and arr[i] < arr[l]:
        largest = l
    # if right child exits
    if r < n and arr[largest] < arr[r]:
        largest = r
    # root
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap
        # root.
        heapUp(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # arrange heap in max order
    for i in range(n,-1,-1):
        heapUp(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i] # swap
        heapUp(arr, i, 0)
    return arr