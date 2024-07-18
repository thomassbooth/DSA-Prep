

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    
    length = 0
    _head = None
    _tail = None

    def __init__(self) -> None:
        self._head, self._tail = None, None
        self.length = 0

    def enqueue(self, item) -> None:
        self.length += 1
        new_node = Node(item)
        if self._tail is None:
            self._tail, self._head = new_node, new_node
            return self._head.value
        
        self._tail.next = new_node
        self._tail = new_node
        return new_node.value
        

    def dequeue(self):
        
        if self._head is None:
            return None
        
        self.length -= 1

        removed_value = self._head.value
        self._head = self._head.next

        if self._head is None:
            self._tail = None
            
        return removed_value
    


    def peak(self):
        return self._head.value
    

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"Peek: {q.peak()}")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()  # Attempt to dequeue from an empty queue
    print(f"Queue size: {q.length}")