class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums:
            return None
        
        middle = len(nums) // 2
        
        root = TreeNode(nums[middle])
        
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])
        
        return root
    
    
nums = [-10,-3,0,5,9]
s = Solution()
s.sortedArrayToBST(nums)