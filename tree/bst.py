# Binary Search Tree is a node-based binary tree data structure which has the following properties:

# The left subtree of a node contains only nodes with keys lesser than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree.

# Требования по методам: вставка и удаление по значению (O(n)), создание дерева из любого списка (O(nlogn)), 
# обходы дерева (3 штуки за O(n) каждый), найти элемент по значению (O(n)), высота ((O(n))

                                                                                  
class Node:
    
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 

class Tree:
    
    def __init__(self, root: Node) -> None:
        self.root = root
        self.parent = None
        
    def insert(self, current, val):
        if self.root is None:
            self.root = Node(val)
            
        else:
            if current.val > val:
                if current.left is None:
                    current.left = Node(val)
                else:
                    self.insert(current.left, val)
            else:
                if current.right is None:
                    current.right = Node(val)
                else:
                    self.insert(current.right, val)
                    

    def delete(self, current: Node, val) -> Node:
    
        if current is None:
            return current
            
        elif val < current.val:
                            
            if current.left.val == val:
                self.parent = current
            
            return self.delete(current.left, val)
            
        elif val > current.val:
            
            if current.right.val == val:
                self.parent = current
                
            return self.delete(current.right, val)
            
        else:
                        
            if current.left and current.right: # a node has 2 children
                
                child = current.right
                
                while child.left:
                    child = child.left
                
                current.val = child.val
                current.right = self.delete(current.right, current.val)
                
                return current

            else: # a node has one child
                
                child = current.left if current.left else current.right # contains children node
                
                if not child:
                    if self.parent.val < val:
                        self.parent.right = None
                
                    else:
                        self.parent.left = None
                        
                else:
                    if self.parent.val < val:
                        self.parent.right = child
                    
                    else:
                        self.parent.left = child
                    
                return self.root


    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
            
            
    def find(self, current: Node, value):
        
        if not current:
            return
        
        if current.val == value:
            print('Found!')
            return current
        
        if value > current.val:
            self.find(current.right, value)
        else:
            self.find(current.left, value)
        
    
    def height(self, current: Node) -> int:
        if current is None:
            return 0
        
        else:
            return 1 + max(self.height(current.left), self.height(current.right))
    
        
    @staticmethod
    def list_to_tree(nums: list, start: int, end: int, flag_sort=True):
        
        if not flag_sort:
            nums = sorted(nums)
        
        def list_to_nodes(nums: list, start: int, end: int) -> Node:
                                
            if not nums or start < 0 or end >= 4 or end < start:
                return None
            
            if start == end:
                res = Node(nums[start])
                return res
            
            middle = int(start + (end - start) / 2)
            
            tree = Node(nums[middle])
            
            tree.left = list_to_nodes(nums, start, middle - 1)
            tree.right = list_to_nodes(nums, middle + 1, end)
            
            return tree
        nodes = list_to_nodes(nums, start, end)

        return Tree(nodes)

s = Tree.list_to_tree([10,20,30,40], 0, 3)
s.inorder(s.root) 
 

t = Tree(Node(50))
t.insert(t.root, 30)
t.insert(t.root, 25)
t.insert(t.root, 20)
t.insert(t.root, 35)
t.insert(t.root, 28)
# t.inorder(t.root)

print('-' * 20)

# Delete node by value
t.root  = t.delete(t.root, 25)
t.inorder(t.root)

# Find
t.find(t.root, 20)

