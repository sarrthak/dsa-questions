class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        fmap = {}
        for i in s:
            if i in fmap:
                fmap[i] += 1
            else:
                fmap[i] = 1
            
        for j in t:
            if j in fmap:
                if fmap[j] > 1:
                    fmap[j] -= 1
                    
                elif fmap[j] == 1:
                    fmap[j] -= 1
                    fmap.pop(j)
        
        
        return fmap == {}
                

s = "racecar"
t = "carrace"

sol = Solution()
print(sol.isAnagram(s, t))