# re

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-0]', '', s)
        
        return s == s[::-1]
        

a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))