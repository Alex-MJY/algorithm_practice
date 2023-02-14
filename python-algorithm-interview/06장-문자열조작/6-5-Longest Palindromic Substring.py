class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1 : right - 1]
        
        if len(s) < 2 or s == s[::-1]: # 예외처리
            return s
        
        result = ''
        
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result
    
    
'''
2칸, 3칸으로 구성된 투 포인터가 슬라이딩 윈도우처럼 전진해 나간다.
이때 윈도우에 들어온 문자열이 팰린드롬인 경우 그 자리에 멈추고, 투 포인터가 점점 확장하는 식이다.
팰린드롬은 짝수일 때도 있고, 홀수일 때도 있다. 

함수가 발산하여 무한 루프에 빠지지 않도록 예외처리를 잊으면 안된다.
'''