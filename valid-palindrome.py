import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1; i = 0
        while i<j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))  # True