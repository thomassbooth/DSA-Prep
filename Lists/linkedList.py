
class LinkedList:

    def __innit__(self, value, head = None):
        self.head: LinkedList = head
        self.next: LinkedList | None = None
        self.tail: LinkedList | None = None
        self.value: str | int| None = value




if "__main__" == __name__:

    #create a linked list
    a = LinkedList(1)
    b = LinkedList(2)
    c = LinkedList(3)
    d = LinkedList(4)

    #link the list
    a.next = b
    b.next = c
    c.next = d

    #print the list
    print(a.value)
    print(a.next.value)
    print(a.next.next.value)
    print(a.next.next.next.value)