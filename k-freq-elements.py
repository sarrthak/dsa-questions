from typing import List
import heapq

"""Time Complexity: O(nlogn) n -> size of list, NOT OPTIMAL"""
# APPROACH 1: Sorting keys in dictionary
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         fmap = {}
#         op = []
#         for i in nums:
#             fmap[i] = 1 + fmap.get(i, 0)        
#         fmap = {k: v for k,v in sorted(fmap.items(), key=lambda item: item[1], reverse=True)}
#         print('fmap: ', fmap)     
#         for key in fmap:
#             if k > 0:
#                 op.append(key)
#             else:
#                 break
#             k -=1    
#         return op

#APPROACH 2: Heap Approach (Time Complexity: O(n + klogm)    
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         if len(nums) == 0 or k == 0:
#             return []
#         fmap = {}
#         for i in nums:
#             fmap[i] = 1 + fmap.get(i, 0)
#         buff: List[tuple] = []
#         for num, freq in fmap.items():
#             tup = (-1 * freq, num)
#             buff.append(tup)
            
#         heapq.heapify(buff)
#         op: List[int] = []
#         for _ in range(k):
#             if buff:
#                 freq, num = heapq.heappop(buff)
#                 op.append(num)
#             else:
#                 break
#         return op


#APPROACH 3: Bucket Sort(Time Complexity: O(n)) (MOST OPTIMAL)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return []
        
        fmap = {}
        for i in nums:
            fmap[i] = 1 + fmap.get(i, 0)
            
        flist = [[] for i in range(len(nums) + 1) ]
        for num, freq in fmap.items():
            flist[freq].append(num)
        
        op: List[int] = []
        for i in range(len(flist)-1, 0,-1):
            for num in flist[i]:
                op.append(num)
                if len(op) == k:
                    return op
        
        return op
                
sol = Solution()
print(sol.topKFrequent([1,2,2,2,3,3,3], 2))