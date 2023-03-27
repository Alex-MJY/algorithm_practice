class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = []
        window = collections.deque()

        cur_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if cur_max == float('-inf'):
                cur_max = max(window)
            elif v > cur_max:
                cur_max = v

            r.append(cur_max)

            # 최댓값이 윈도우에서 빠지면 초기화
            if cur_max == window.popleft():
                cur_max = float('-inf')
        return r