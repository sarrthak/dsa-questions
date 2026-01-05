from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        num_set = set(nums)
        longest = 0
        for n in num_set:
            length = 0
            if n - 1 not in num_set:
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest
            
        
    

sol = Solution()
print(sol.longestConsecutive(nums=[2,20,4,10,3,4,5]))
print(sol.longestConsecutive(nums=[0,3,2,5,4,6,1,1]))
print(sol.longestConsecutive(nums=[]))
print(sol.longestConsecutive(nums=[9,1,4,7,3,-1,0,5,8,-1,6]))
print(sol.longestConsecutive(nums=[1]))