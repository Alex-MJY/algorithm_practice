# list

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s:
            if i.isalnum():
                l.append(i.lower())
                    
        # if l == l[::-1]:
        #     return True
        # else:
        #     return False
        
        while len(l) > 1:
            if l.pop(0) != l.pop():
                return False
        return True