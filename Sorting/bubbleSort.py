

def bubbleSort(arr):
    n = len(arr)
    #we need to loop through the array the length of it
    for i in range(n):
        #we shrink the array each time by 1, including the first so we dont get index error since we look at the index after last
        for j in range(0, n-i-1):
            #if element before the next is greater then swap
            if arr[j] > arr[j+1]: arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr



if "__main__" == __name__:
    print(bubbleSort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) #1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(bubbleSort([64, 34, 25, 12, 22, 11, 90])) #11, 12, 22, 25, 34, 64, 90