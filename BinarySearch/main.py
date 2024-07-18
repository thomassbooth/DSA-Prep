import math

def binary_search(arr, target):
    low = 0
    high = len(arr);

    while low < high:
        #find out mid point
        mid = math.floor(low + (high-low)/2) 
        value = arr[mid]
        print('mid:', mid, 'low:', low, 'high:', high, 'value:', value)
    
        #check if the value at this mid point is equal to target
        if (value == target):
            return True
        #if the value is greater than the target then search the left half
        elif (value > target):
            high = mid
        else:
            low = mid + 1

    return False


if __name__ == "__main__":

    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))

