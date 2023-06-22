# pythonic
class Solution1:
    def reverseString(self, s: list) -> None:
        return s.reverse()


# two pointer
class Solution2:
    def reverseString(self, s: list) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s