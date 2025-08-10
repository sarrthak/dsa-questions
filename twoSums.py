from typing import List

"""to solve this question we need to check if the  """
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [nums.index(complement), i]
            seen.append(nums[i])
    

sol = Solution()
print(sol.twoSum([1,3,3], 6))