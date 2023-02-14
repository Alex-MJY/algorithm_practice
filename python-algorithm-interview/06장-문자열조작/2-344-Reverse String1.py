class Solution:
    def reverseString(self, s):
        #Do not return anything, modify s in-place instead.
        
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
        
s = ["h","e","l","l","o"]
sol = Solution()
print(sol.reverseString(s))

'''
문자열을 뒤집을 때엔 포인터(left, right)를 사용하면 쉽다.
하나의 배열에서 두 개 이상의 인덱스값을 비교해야 할 땐 포인터가 유용하다.

** 파이썬 내부함수인 reverse()를 이용해도 된다.
'''