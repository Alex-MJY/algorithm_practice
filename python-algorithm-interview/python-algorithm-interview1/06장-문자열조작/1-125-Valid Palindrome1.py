class Solution:
    def isPalindrome(self, s):
        strs = []
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s))

'''
문자열을 조작하는 알고리즘은 문자열을 필터링 해야하고, 필터링한 변수들을 담을 바구니가 필요하다.
대부분 list(array)를 쓰지만 순서를 정해줘야 할 경우 dictonary도 사용한다.

pop()을 통해 앞, 뒤의 문자를 비교할 경우 pop(0)은 O(n)의 시간을 들기 때문에
collections.deque()를 통해 시간을 단축할 수 있다.

isalnum() == 변수가 문자열 or 숫자면 True
isalpha() == 변수가 문자열(영어 혹은 한글)이면 True
isdigit() == 변수가 숫자면 True 

문자열을 다루기 가장 쉬운 방법은 슬라이싱이나 정규식을 사용하는 것인데,
가시성이 안좋을 수 있다.
'''