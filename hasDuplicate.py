from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        fmap = {}
        count = 1
        for i in nums:
            if(i in fmap):
                return True
            
            else:
                fmap[i] = 1
            
        return False
    
nums = [1,2,3,3]
sol = Solution()
print(sol.hasDuplicate(nums))