class Node:

    def __init__(self, value):
        self.value = value
        self.previous = None


class Stack:


    def __init__(self) -> None:
        self._head = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        self.length += 1
        #no head
        if self._head == None:
            self._head = newNode
            return self._head.value

        #if a head is set, set the old head to be the previous of the new head
        newNode.previous = self._head
        self._head = newNode
    
        return newNode.value
        

    def pop(self):
        
        if self._head is None:
            return None
        
        self.length -= 1

        removedValue = self._head.value

        self._head = self._head.previous

        return removedValue

    def peak(self):
        
        return self._head.value


if __name__ == "__main__":
    # Create a stack
    stack = Stack()

    # Push elements onto the stack
    print(f"Pushed: {stack.push(1)}")  # Output: Pushed: 1
    print(f"Pushed: {stack.push(2)}")  # Output: Pushed: 2
    print(f"Pushed: {stack.push(3)}")  # Output: Pushed: 3

    # Peek the top element of the stack
    print(f"Peek: {stack.peak()}")  # Output: Peek: 3

    # Pop elements from the stack
    print(f"Popped: {stack.pop()}")  # Output: Popped: 3
    print(f"Popped: {stack.pop()}")  # Output: Popped: 2
    print(f"Popped: {stack.pop()}")  # Output: Popped: 1

    # Try to pop from an empty stack
    print(f"Popped: {stack.pop()}")  # Output: Popped: None