class Solution:
    def searchMatrix(self, matrix: list, target: int):
        return any(target in row for row in target)