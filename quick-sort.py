from typing import List

class Solution: 
    def sortArray(self, nums: List[int]) -> None:
        # def quickSort(lo: int, high: int) -> None:
        #     """this hoare's partition technique which allows for in place 
        #     swapping without needing any auxillary space. 
            
        #     WILL GIVE TLE ON LEETCODE. 
        #     Time Complexities:
        #     (1) Worst Case = O(n^2)
        #     (2) Best Case = O(nlogn)
        #     (3) Average Case = O(nlogn)
        
        #     Args:
        #         lo (int): starting point of the partition
        #         high (int): end of partition
        #     """
        #     if lo >= high:
        #         return 
            
        #     pivot = nums[(lo + high) // 2]
        #     i = lo 
        #     j = high
            
        #     while i <= j:
        #         while i <= high and nums[i] < pivot: 
        #             i += 1
                
        #         while j >= lo and nums[j] > pivot:
        #             j -= 1
                
        #         if i <= j:
        #             nums[j], nums[i] = nums[i], nums[j]
        #             i += 1
        #             j -= 1
            
        #     quickSort(i, high)
        #     quickSort(lo, j)
        def mergeSort(nums: List[int]) -> List[int]:
            def merge(left: List[int], right: List[int]) -> List[int]:
                res = []
                i = j = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        res.append(left[i])
                        i += 1
                    else:
                        res.append(right[j])
                        j += 1
                
                res.extend(left[i:])
                res.extend(right[j:])

                return res

            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
        return mergeSort(nums)

        
sol = Solution()
print(sol.sortArray(nums=[1,0,1,2]))