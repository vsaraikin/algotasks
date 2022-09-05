class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def __init__(self) -> None:
        self.c = 0
    
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        
        if root.left is None and root.right is None and targetSum == root.val:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) and self.hasPathSum(root.right, targetSum - root.val)
        


s = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.left.right = TreeNode(4)
root.right.left.right.right = TreeNode(1)
print(s.hasPathSum(root, 22))