import re

class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
        
        # if s == s[::-1]:
        #     return True
        # else:
        #     return False
        
s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))