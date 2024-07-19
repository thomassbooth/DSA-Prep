from binaryTree import Node, BinaryTree
from collections import deque


#1 add the head to the queue
#2 while the queue is not empty
#3 pop the leftmost (in the first instance it would be the head)
#4 check if the value is what we want
#5 if not then we add the left and the right nodes to the end of the queue
#6 we still need to check teh level as its a queue, left and right are added first

def bfs(head, findValue):
    
    #initialate a queue with the first element being the head of the tree
    q = deque([head])

    while len(q):
        #pop the leftmost element ()
        curr = q.popleft()
        
        #check if the value were looking for 
        if curr.val == findValue:
            return True
        
        #if not then we need to add the left and the right nodes to the queue
        if curr.left:
            q.append(curr.left)

        if curr.right:
            q.append(curr.right)

    return False

    


if "__main__" == __name__:

    # Create a binary tree
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("Preorder traversal of binary tree is")
    print(bfs(tree.root, 6))
    print()