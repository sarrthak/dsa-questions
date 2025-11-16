from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #handling edge case
        if (len(nums) == 0):
            return []
        
        #count zeroes
        ind_zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                ind_zeroes.append(i)
        
        if len(ind_zeroes) > 1:
            return [0] * len(nums)
                
        prd = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                prd *= nums[i]
            else:
                continue
        
        
        op = [-1] * len(nums)
        if len(ind_zeroes) == 1:
            op = [0] * len(nums)
            op[ind_zeroes[0]] = prd
            return op
            
        
        for i in range(len(nums)):
            op[i] = prd // nums[i]
        
        return op
        
        
sol = Solution()
#print(sol.productExceptSelf([1,2,4,6]))
print(sol.productExceptSelf([-1,0,1,2,3]))
print(sol.productExceptSelf([0,0,0]))
print(sol.productExceptSelf([0,8,0]))
