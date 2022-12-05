class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
flag = True


class Solution:
    
    def __init__(self):
        self.m2 = 1

    def maxDepth(self,root):
        if root is None or isinstance(root, int):
            return 0
        else:
            res = 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
            
            if res > self.m2:
                self.m2 = res
            
            if self.m2 - res >= 2:
                flag = False
            
            return res
        

    def isBalanced(self, root: TreeNode) -> bool:
        if not flag:
            return False
        
        if root is None:
            return True

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        
        if left - right > 1 or right - left > 1:
            return False
        
        # recursion check
        left_node = self.isBalanced(root.left)
        right_node = self.isBalanced(root.right)
        
        if left_node == True and right_node == True:
            return True
        else:
            return False
        

        
        

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(3)
# root.left.left.left = TreeNode(3)
# root.left.left.right = TreeNode(3)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(9)


s = Solution()
print(s.isBalanced(root))