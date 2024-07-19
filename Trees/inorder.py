from binaryTree import Node, BinaryTree

def walk(node, path: list):
     
    #base case, node doesnt exist so we can return

    if not node:
        return path
    
    #pre
    walk(node.left, path)
    #recurse
    
    path.append(node.val)
    walk(node.right, path)
    #post
    return path

    


if "__main__" == __name__:

    # Create a binary tree
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print("Preorder traversal of binary tree is")
    print(walk(tree.root, []))
    print()