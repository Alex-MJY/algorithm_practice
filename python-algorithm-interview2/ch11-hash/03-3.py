'''중복 문자가 없는 가장 긴 부분 문자열(substring)의 길이를 리턴하라.'''

# 슬라이딩 윈도우와 투 포인터로 사이즈 조절
# 포인터 2개 모두 왼쪽에서 출발한다. (start, index)
# 이미 등장한 문자라면 used에 있을 것이고, start를 used[char] + 1 위치로 갱신한다. 
# 처음 보는 문자라면, 매번 max()로 부분 문자열의 길이를 확인하면서 더 큰 값인 경우 갱신한다.
# used[char]는 현재 문자를 키로 하는 해시 테이블이며, 현재 위치를 값으로 삽입한다.
# start = used[char] + 1은 '현재 위치 + 1'이 되고 이미 등장했던 문자인 경우, 왼쪽 포인터인 start를
# 현재 위치까지 옮기게 된다. 슬라이딩 바깥에 있는 문자는 예전에 등장한 적이 있더라도 지금은 무시해야 한다.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length