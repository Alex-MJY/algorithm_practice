# ascending order
class Solution1:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        array = []
        for i in nums:
            array.append(i)
            if len(array) == 2:
                result += min(array)
                array = []
        return result


# Calculate the even-numbered value
class Solution2:
    def arrayPairSum(self, nums: list) -> int:
        result = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum


# pythoninc
class Solution3:
    def arrayPairSum(self, nums: list) -> int:
        return sum(sorted(nums)[::2])