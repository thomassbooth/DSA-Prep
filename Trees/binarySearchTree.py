from binaryTree import Node, BinaryTree

def search(curr, findValue):
    
    #base case
    if curr is None: return False
    
    if curr.val == findValue: return True

    #recurse
    if findValue > curr.val: return search(curr.right, findValue)
    
    return search(curr.left, findValue)


if __name__ == "__main__":

    # Manually creating a binary search tree
    tree = BinaryTree()
    tree.root = Node(7)
    tree.root.left = Node(3)
    tree.root.right = Node(10)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(8)
    tree.root.right.right = Node(12)

    # Test the search function
    test_values = [5, 8, 13, 1, 6]
    for val in test_values:
        result = search(tree.root, val)
        print(f"Searching for {val}: {'Found' if result else 'Not Found'}")
