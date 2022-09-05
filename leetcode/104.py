class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.c = 0
    
    def maxDepth(self, root: TreeNode):
        
        if isinstance(root, int):
            return self.c
        
        if isinstance(root, type(None)):
            return self.c
        
        if root.left != None or root.right != None:
            self.c += 1
            
        return max(self.maxDepth(root.left) and self.maxDepth(root.right))
    
    
root = TreeNode(3)
root.left = 9
root.right = TreeNode(20)
root.right.left = None
root.right.right = 7

s = Solution()
print(s.maxDepth(root))
