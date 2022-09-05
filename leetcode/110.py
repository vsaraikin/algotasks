class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:

    def maxDepth(self,root):
        if root is None or isinstance(root, int):
            return 0
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        

    def isBalanced(self, root: TreeNode) -> bool:
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
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.isBalanced(root))