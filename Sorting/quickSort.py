


def quickSort(arr, lo, hi):

    #base cases
    if (lo >= hi):
        return
    
    pivotIndx = partition(arr, lo, hi)

    #we split the array into two parts
    #pivotIndx -1 as we dont include the pivot value in the subarrays
    quickSort(arr, lo, pivotIndx - 1) #left side of the array exluding pivot
    quickSort(arr, pivotIndx + 1, hi) #right side of the array excluding pivot
    
    return arr


def partition(arr, lo, hi):
    #can be anything, im chosing the rightest side
    pivot = arr[hi]

    indx = lo - 1

    #walk from lo to the hi but not including the hi - its our pivot
    for i in range(lo, hi-1):
        #we are moving everything lower than our pivot to the left
        #we keep recursively doing this
        if (arr[i] <= pivot):
            #we swapped one so we move the index up
            indx += 1
            arr[indx], arr[i] = arr[i], arr[indx]

    indx += 1

    #we need to move our pivot value to where our index is
    arr[hi] = arr[indx]
    arr[indx] = pivot

    return indx


if "__main__" == __name__:
    print(quickSort([3, 4, 1, 9, 8, 12, 2], 0, 6))
    print(quickSort([3, 4, 1, 3, 9, 8, 12, 2], 0, 7))
