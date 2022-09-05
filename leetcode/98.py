class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isValidBST(self, root: TreeNode, lower_bound=-1e12, upper_bound=1e12) -> bool:
        
        if root is None or isinstance(root, list):
            return True
        
        if root.val <= lower_bound or root.val >= upper_bound:
            return False
        

        return self.isValidBST(root.left, lower_bound, root.val) and self.isValidBST(root.right, root.val, upper_bound)
    

s = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(s.isValidBST(root))
