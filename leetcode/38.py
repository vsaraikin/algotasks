# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

class Solution:
    
    def name_a_next_thing(self, s: str) -> list:
        char_list = [x for x in s]
        res = ''
        tmp_c = 1
        prev = None
        
        for n in char_list:
            
            if prev:
                if prev == n:
                    tmp_c += 1
                else:
                    res += str(tmp_c) + prev
                    prev = n
                    tmp_c = 1
            else:
                prev = n
            
        res += str(tmp_c) + prev   
        return res
    

    def countAndSay(self, n: int) -> str:
        
        res = '1'
        for _ in range(2, n+1):
            res = self.name_a_next_thing(res)
        
        return res    

s = Solution()
print(s.countAndSay(6))
