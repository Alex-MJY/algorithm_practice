'''가장 긴 팰린드롬 부분 문자열을 출력하라.'''

# two pointer가 중앙을 중심으로 확장하는 형태의 함수를 따로 만듬
# 문자가 짝수일 경우(i, i+1), 홀수일 경우(i, i+2)를 모두 체크해서 len의 max값을 추출

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1 : right - 1]

        if len(s) < 2 or s == s[::-1]: 
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result,
                        expand(i, i + 1),
                        expand(i, i + 2),
                        key = len)
        return result