class BinaryTree:
    
        def __init__(self):
            self.root: None | Node = None
    

class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

