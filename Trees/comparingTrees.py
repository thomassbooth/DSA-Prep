from binaryTree import Node, BinaryTree

def compare_dfs(a: Node | None, b: Node | None) -> bool:

    if a == None and b == None: return True
    #check if both nodes are None
    if a == None or b == None: return False
    
    #check if they are not the same
    print(a.val, b.val)
    if a.val != b.val: return False
    
    #recurse
    # left = compare_dfs(a.left, b.left)
    # if (not left): return False

    # right = compare_dfs(a.right, b.right)
    # if (not right): return False

    # return True

    return compare_dfs(a.left, b.left) and compare_dfs(a.right, b.right)



if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree2 = BinaryTree()
    tree2.root = Node(1)
    tree2.root.left = Node(2)
    tree2.root.right = Node(3)
    tree2.root.left.left = Node(4)
    tree2.root.left.right = Node(5)

    tree3 = BinaryTree()
    tree3.root = Node(1)
    tree3.root.left = Node(2)
    tree3.root.right = Node(3)
    tree3.root.left.left = Node(4)
    tree3.root.left.right = Node(6)
    tree3.root.right.left = Node(5)


    print(compare_dfs(tree.root, tree2.root))
    print(compare_dfs(tree.root, tree3.root))
    print()