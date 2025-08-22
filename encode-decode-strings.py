from typing import List

# The below is a primitive implementation for the encode and decode question. 
# Time Complexity - O(n)
# The below implementation fails for test cases - ["a1", "b"], and the functions are not inverse of each other. 
class Solution:
    def encode(self, strs: List[str]) -> str:
        op: str = ""
        for i in strs:
            op += i + str(len(i))
        return op
            
    def decode(self, s: str) -> List[str]:
        op: List[str] = []
        buff: str = ""
        for i in s:
            if i.isdigit():
                op.append(buff)
                buff = ""
                continue
            else:
                buff = buff + i
        
        return op
        

sol = Solution()
encodedString = sol.encode(["a1", "b"])
print(sol.decode(encodedString))