""" Binary search tree, search: O(h), insertion: O(h), deletion: O(h),
    where h is the height of the tree. Note that O(h) = O(n) if the
    tree is skewed. """

class Node:
    
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.val = key 

class BST:

    def __init__(self):
        self.root = None
        

    def insert(self, key):
        
        node = Node(key)
        
        if self.root is None:
            self.root = node
        else: 
            self.binaryInsert(self.root, node)

    def binaryInsert(self, root, node):

        if root is None:
            root = node
        else:
            if root.val > node.val:
                if root.left is None:
                    root.left = node
                else:
                    self.binaryInsert(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.binaryInsert(root.right, node)

    def search(self, key):
        return self.binarySearch(self.root, key)

    def binarySearch(self, root, key):

        if root is None or root.val == key:
            return root

        if root.val < key:
            return self.binarySearch(root.right, key)

        return self.binarySearch(root.left, key)

    def inOrderWalk(self):
        self.inOrder(self.root)
        
    def inOrder(self, root):

        if root:
            self.inOrder(root.left)
            print(root.val)
            self.inOrder(root.right)

  
bst = BST()
bst.insert(50)
bst.insert(30) 
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

bst.inOrderWalk()
