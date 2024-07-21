
class Node: 

    def __init__(self, value, ) -> None:
        self.value = value,
        self.next = None
        self.prev = None


class LRU:

    def __init__(self, capacity = 10) -> None:
        self._length = 0
        self._capacity = capacity
        self._head: Node | None = None
        self._tail: Node | None = None
        self._lookup: dict = {} # {key: Node}
        self._reverseLookup: dict = {} # {Node: key}

    #removes our node from the linked list
    def _detach(self, node) -> None:
        
        #if we have a previous node, we need to update its next to be the next node from the one we want to remove
        if node.prev: node.prev.next = node.next

        #if we dont have a previous node we are the head and dont need to change it
        #if our next exists then opposite direction
        if node.next: node.next.prev = node.prev

        if self._head == node: self._head = self._head.next

        if self._tail == node: self._tail = self._tail.prev
        

    def _trimCache(self) -> None:
        
        #capacity hasnt been reached
        if self._length <= self._capacity: return

        #remove the last node
        tail = self._tail
        self._detach(self._tail)

        key = self._reverseLookup.get(tail)
        del self._lookup[key]
        self._length =- 1

    #adds our node to the front of the linked list
    def _prepend(self, node) -> None:
        
        if self._head is None: 
            self._head, self._tail = node, node
            return

        #old head becomes our new nodes next
        node.next = self._head
        #our current heads previous becomes our new node as we are replacing the head with it
        self._head.prev = node

        self._head = node


    def update(self, key, value):

        # does it exist?
        node = self._lookup.get(key, None)
        if not node: 
            node = Node(value)
            self._length += 1
            self._prepend(node)
            self._trimCache()

            self._lookup.update({key: node})
            self._reverseLookup.update({node: key})
        else:
            self._detach(node)
            self._prepend(node)
            node.value = value
        

        # get()
        # if it doesnt, check capacity and evict the last in the LRU, insert new at the front

        # if it does, update the value and move it to the front

        pass

    def get(self, key):
        # check cache for existance

        node = self._lookup.get(key, None)
        if not node: return None

        # then move it to the front since its the most recently used
        self._detach(node)
        self._prepend(node)
        # return out the value found or undefined if not exist
        return node.value
    

def test_lru_cache():
    cache = LRU(3)
    
    # Test case 1: Adding items to the cache
    cache.update('a', 1)
    cache.update('b', 2)
    cache.update('c', 3)
    
    assert cache.get('a') == 1, "Test case 1 failed"
    assert cache.get('b') == 2, "Test case 1 failed"
    assert cache.get('c') == 3, "Test case 1 failed"
    
    # Test case 2: Cache capacity and eviction
    cache.update('d', 4)
    
    assert cache.get('a') is None, "Test case 2 failed"  # 'a' should be evicted
    assert cache.get('b') == 2, "Test case 2 failed"
    assert cache.get('c') == 3, "Test case 2 failed"
    assert cache.get('d') == 4, "Test case 2 failed"
    
    # Test case 3: Updating existing item
    cache.update('b', 20)
    
    assert cache.get('b') == 20, "Test case 3 failed"
    assert cache.get('c') == 3, "Test case 3 failed"
    assert cache.get('d') == 4, "Test case 3 failed"
    
    # Test case 4: Access order after retrieval
    cache.get('c')  # 'c' should now be the most recently used
    
    cache.update('e', 5)
    
    assert cache.get('b') == 20, "Test case 4 failed"
    assert cache.get('c') == 3, "Test case 4 failed"
    assert cache.get('d') is None, "Test case 4 failed"  # 'd' should be evicted
    assert cache.get('e') == 5, "Test case 4 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_lru_cache()