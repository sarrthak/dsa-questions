from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        op: str = ""
        for i in strs:
            op += i + "."
        return op
            
    def decode(self, s: str) -> List[str]:
        return s.split(".")[:-1]
        

sol = Solution()
encodedString = sol.encode(["neet","code","love","you"])
print(sol.decode(encodedString))