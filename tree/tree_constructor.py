class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, sorted_array: list):
        if sorted_array == sorted(sorted_array):
            self.sorted_array = sorted_array
        else:
            print('Array is not sorted -> sorting')
            self.sorted_array = sorted(sorted_array)
    
    def creator(self) -> TreeNode:
        return self.sortedArrayToBST(self.sorted_array)
    
    def sortedArrayToBST(self, sorted_array) -> TreeNode:
        if not sorted_array:
            return None
        
        middle = len(sorted_array) // 2
        
        root = TreeNode(sorted_array[middle])
        
        root.left = self.sortedArrayToBST(sorted_array[:middle])
        root.right = self.sortedArrayToBST(sorted_array[middle+1:])
        
        return root
    
    
nums = [-10,-3,0,5,9]
s = Solution(nums)
s.creator()
