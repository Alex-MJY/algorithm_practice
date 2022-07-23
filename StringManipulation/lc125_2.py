# deque

from matplotlib import collections


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
                
        if strs == strs[::-1]:
            return True
        else:
            return False
                    