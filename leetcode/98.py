class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isValidBST(self, node: TreeNode, lower_bound=-1e6, upper_bound=1e6) -> bool:
            if not node:
                return True
            
            if lower_bound is not None and node.val <= lower_bound:
                return False
            
            if upper_bound is not None and node.val >= upper_bound:
                return False
            

            return self.isValidBST(node.left, lower_bound, node.val) and self.isValidBST(node.right, node.val, upper_bound)
    
    

s = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(s.isValidBST(root))
