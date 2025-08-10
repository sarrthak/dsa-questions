from typing import List

class Solution:
    def checkAnagram(str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False
        
        fmap = {}
        for i in str1:
            if i in fmap:
                fmap[i] += 1
            else:
                fmap[i] = 1
        

        for j in str2:
            if j in fmap and fmap[j] > 1:
                fmap[j] -= 1
            elif j in fmap and fmap[j] == 1:
                fmap.pop(j)
            else:
                return False
        
        return fmap == {}

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = []
        if len(strs) == 1:
            return [strs[0]]
        
        if len(strs) == 0:
            return []
        
        visited = set()
        
        for i, word in enumerate(strs):
            if i in visited:
                continue
            buffer = [word]
            visited.add(i)
            for j in range(i+1, len(strs)):
                if j not in visited and Solution.checkAnagram(strs[j], word):
                    buffer.append(strs[j])
                    visited.add(j)
            op.append(buffer)
    
        return op
        
    
sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))