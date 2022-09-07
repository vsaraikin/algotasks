class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self, value) -> None:
        self.root = Node(value)    
    
    
    def inorder(self, root) -> None:
        if root is not None:
            self.inorder(root.left)

            print(root.key)

            self.inorder(root.right)


    def insert(self, node, key) -> Node:

        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        return node
    
    def maxDepth(self, root: Node) -> int:
        
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


tree = Tree(4)
tree.insert(tree.root, 8)
tree.insert(tree.root, 3)
tree.insert(tree.root, 1)

print("Traversing:")
tree.inorder(tree.root)

print("Max depth of tree:", tree.maxDepth(tree.root))