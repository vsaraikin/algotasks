from typing import List
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank_custom = set(bank)
        q = deque([(startGene, 0)])
        
        while q:
            current, steps = q.popleft()
            
            if current == endGene:
                return steps
            
            for i in range(8):
                for char in 'ACGT':
                    tmp = current[:i] + char + current[i + 1:]
                    
                    if tmp in bank_custom:
                        bank_custom.remove(tmp)
                        q.append((tmp, steps + 1))    
        
        return -1
        
                
        
        
        
        
s = Solution()
# l1 = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]
# l2 = ["AATCTTGG", "AATTTTGG", "AATTCTGG", "AATTCCGG"]
# print(s.minMutation("AACCTTGG", "AATTCCGG", l2))
print(s.minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]))
