from typing import List
import collections

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
          count = collections.Counter(nums)
          
          for k,v in count.items():
              if v > 1:
                  return k
    
sol = Solution()
print(sol.hasDuplicate(nums = [1,2,3,3]))