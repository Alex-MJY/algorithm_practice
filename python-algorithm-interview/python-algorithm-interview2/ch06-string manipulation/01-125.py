'''주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다'''

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        # filtering
        array = []
        for char in s:
            if char.isalnum():
                array.append(char.lower())

        # check palindrome
        while len(array) > 1:
            if array.pop(0) != array.pop():
                return False
        return True
    


# 리스트의 pop(0)은 시간복잡도가 O(n)이고 데크의 popleft() O(1)이다.
import collections    
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        # filtering
        array = collections.deque()
        for char in s:
            if char.isalnum():
                array.append(char.lower())

        # check palindrome
        while len(array) > 1:
            if array.popleft() != array.pop():
                return False
        return True
    
    

# pythonic solivng : slicing
# solution2보다 2배 정도 속도를 높일 수 있다.
import re
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]