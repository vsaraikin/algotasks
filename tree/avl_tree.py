from bst import Tree

# AVL tree is a self-balancing binary search tree.
# In an AVL tree, the heights of the two child subtrees of any node differ by at most one; 
# if at any time they differ by more than one, rebalancing is done to restore this property. 

# Differences between Binary Search tree and AVL tree
# In the AVL tree, each node contains a balance factor, and the value of the balance factor must be either -1, 0, or 1. 
# Every Binary Search tree is not an AVL tree because BST could be either a balanced or an unbalanced tree.

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        

class AVL_Tree(Tree):
            
    def __init__(self, root: Node) -> None:
        self.root = root
    
    
    def lr(self, current):
        tmp_right = current.right
        tmp_right_left = tmp_right.left
        tmp_right.left = current
        current.right = tmp_right_left
        
        current.height = 1 + max(self.get_current_height(current.left), self.get_current_height(current.right))
        tmp_right.height = 1 + max(self.get_current_height(tmp_right.left), self.get_current_height(tmp_right.right))
        
        return tmp_right
 
     
    def rr(self, current):
        tmp_left = current.left
        tmp_left_right = tmp_left.right
        tmp_left.right = current
        current.left = tmp_left_right
        
        current.height = 1 + max(self.get_current_height(current.left), self.get_current_height(current.right))
        tmp_left.height = 1 + max(self.get_current_height(tmp_left.left), self.get_current_height(tmp_left.right))
        
        return tmp_left
         
    
    def get_current_height(self, current):
        if not current:
            return 0
        
        return current.height
 
 
    def balance_factor(self, current):
        if not current:
            return 0
        
        return self.get_current_height(current.left) - self.get_current_height(current.right)
    
    
    def min_value(self, current):
        if not current or not current.left:
            return current
        
        return self.min_value(current.left)
     
    
    def insert(self, current, value):
 
        if not current:
            return Node(value)
        
        elif value < current.val:
            current.left = self.insert(current.left, value)
        else:
            current.right = self.insert(current.right, value)
 
        current.height = 1 + max(self.get_current_height(current.left), self.get_current_height(current.right))
 
        bf = self.balance_factor(current)
        if bf > 1:
            if value < current.left.val:
                return self.rr(current)
            else:
                current.left = self.lr(current.left)
                return self.rr(current)
 
        if bf < -1:
            if value > current.right.val:
                return self.lr(current)
            else:
                current.right = self.rr(current.right)
                return self.lr(current)

        self.root = current
        return current
     
     
    def delete(self, current, value):
 
        if not current:
            return current
        
        elif value < current.val:
            current.left = self.delete(current.left, value)
        
        elif value > current.val:
            current.right = self.delete(current.right, value)
        
        else:
            
            if not current.left:
                tmp = current.right
                current = None
                return tmp
            
            elif not current.right:
                tmp = current.left
                current = None
                return tmp
            
            tmp = self.min_value(current.right)
            current.val = tmp.val
            current.right = self.delete(current.right, tmp.val)
        
        current.height = 1 + max(self.get_current_height(current.left), self.get_current_height(current.right))
        bf = self.balance_factor(current)
 
        if bf > 1:
            
            if self.balance_factor(current.left) >= 0:
                return self.rr(current)
            
            else:
                current.left = self.lr(current.left)
                return self.rr(current)
        
        if bf < -1:
            
            if self.balance_factor(current.right) <= 0:
                return self.lr(current)
            
            else:
                current.right = self.rr(current.right)
                return self.lr(current)

        return current
                    
t = AVL_Tree(Node(50))
t.insert(t.root, 30)
t.insert(t.root, 25)
t.insert(t.root, 20)
t.insert(t.root, 35)
t.insert(t.root, 28)
t.delete(t.root, 25) 
t.inorder(t.root)