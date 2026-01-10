from typing import List
"""This is the sorting colors question. 
Which requires us to use an inplace sorting algorithm. I have used merge sort, 
because its TC is O(nlogn) for avg. case, best case and worst case. 

we can use Dutch National Flag algo also, which works by having 3 distinct pointers.
Low, mid and High. Low and Mid point to the start of the array.
    Low - Position to upend 0s
    Mid - track the current number
    High position to upend 2s

Returns:
    _type_: _description_
    """
class Solution:
    # def mergeSort(nums: List[int]) -> None:
    #     def merge(left: List[int], right: List[int]) -> List[int]:
    #         res = []
    #         i = j = 0

    #         while i < len(left) and j < len(right):
    #             if left[i] < right[j]:
    #                 res.append(left[i])
    #                 i += 1
    #             else:
    #                 res.append(right[j])
    #                 j += 1
                
    #         res.extend(left[i:])
    #         res.extend(right[j:])

    #         return res
    #     if len(nums) <= 1:
    #         return nums
        
    #     mid = len(nums) // 2
    #     left = Solution.mergeSort(nums[:mid])
    #     right = Solution.mergeSort(nums[mid:])
    #     return merge(left, right)
    
    def kdnf(nums: List[int], k: int) -> None:
        """this is DNF for k i/ps

        Args:
            nums (List[int]): _description_
            k (int): _description_

        Returns:
            _type_: _description_
        """
        cnt = [0] * k
        for i in nums:
            cnt[i] += 1
        
        j = 0
        for i in range(len(cnt)):
            for _ in range(cnt[i]):
                nums[j] = i
                j += 1
    
    
    def dnf(nums: List[int]) -> None:
        mid = 0
        low = 0
        hi = len(nums) - 1
        
        while mid <= hi:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
            else:
                mid += 1
        
        
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        Solution.dnf(nums)
            
sol = Solution()
nums=[1,0,1,2]
sol.sortColors(nums)
print(nums)