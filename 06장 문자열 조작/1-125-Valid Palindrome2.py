import collections

class Solution:
    def isPalindrome(self, s):
        strs = collections.deque()
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))


# pop(0)이 O(n)인 데 반해, deque의 popleft()는 O(1)이기 때문에 5배 정도 더 빠르다.