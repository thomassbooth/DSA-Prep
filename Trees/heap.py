import math
class MinHeap:

    length = 0
    _data = []

    def __init__(self) -> None:
        self._data = []
        self.length = 0

    def _heapifyDown(self, indx):
        left_indx = self._leftChild(indx)
        right_indx = self._rightChild(indx)

        #dont want to heapify off our array
        #we always fill in left to right, if its greater than or equal, weve left where our heap nodes are
        if indx >= self.length or left_indx >= self.length: return

        rightVal = self._data[right_indx]
        leftVal = self._data[left_indx]
        currentVal = self._data[indx]
        #if our left child is less than our right val, and our current val is greater than left val we swap and keep heapifying
        if leftVal > rightVal and currentVal > rightVal:
            self._data[right_indx], self._data[indx] = currentVal, rightVal
            self._heapifyDown(right_indx)

        elif leftVal < rightVal and currentVal > leftVal:
            self._data[left_indx], self._data[indx] = currentVal, leftVal
            self._heapifyDown(left_indx)



    def _heapifyUp(self, indx):
        #we move this value untill it is the smallest value in the heap

        #top node cant keep going up so we stop at 0
        if indx == 0: return

        #get our parent index + val, check if we are larger than it

        parent_indx = self._parent(indx)
        parent_val = self._data[parent_indx]
        current_val = self._data[indx]

        #if parent val is greater than us
        if parent_val > current_val:
            #swap the two items recursively so it gets moved to the top value
            self._data[parent_indx], self._data[indx] = current_val, parent_val 
            self._heapifyUp(parent_indx)

    
    def _parent(self, indx) -> int:
        #formula is (i-1)/2
        return math.floor((indx-1)/2)
        
    def _leftChild(self, indx) -> int:
        #formula is 2i + 1
        return (2*indx) + 1
    
    def _rightChild(self, indx) -> int:
        #formula is (2i +2)
        return (2*indx) + 2
    
    def insert(self, val):
        self._data.append(val)
        #now we need to heapify up
        self._heapifyUp(self.length)
        self.length += 1

    def delete(self, ):
        #base case
        if (self.length == 0): return None
    
        out = self._data[0]
        self.length -= 1

        if (self.length == 0):
            return self._data.pop()
        
        #delete our node, swap the last element in the array and put it into the first position
        self._data[0] = self._data[self.length]
        self.length -= 1
        self._heapifyDown(0)

        return out
        

if __name__ == "__main__":
    heap = MinHeap()
    values_to_insert = [3, 1, 6, 5, 2, 4]
    for value in values_to_insert:
        heap.insert(value)
        print(f"Heap after inserting {value}: {heap._data}")

    print(f"Deleted element: {heap.delete()}")
    print(f"Heap after deleting: {heap._data}")
    


