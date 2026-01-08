from typing import List

class Solution: 
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(lo: int, high: int) -> None:
            if lo >= high:
                return 
            
            pivot = nums[(lo + high) // 2]
            i = lo 
            j = high
            
            while i <= j:
                while i <= high and nums[i] < pivot: 
                    i += 1
                
                while j >= lo and nums[j] > pivot:
                    j -= 1
                
                if i <= j:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
                    j -= 1
            
            quickSort(i, high)
            quickSort(lo, j)
        
        quickSort(0, high=len(nums) - 1)
        return nums
        
sol = Solution()
# print(sol.sortArray(nums=[10,9,8,6,7]))
print(sol.sortArray(nums=[5,3,8,6,2,7,4,1]))