class Solution:
    def searchMatrix(self, matrix: list, target: int):
        # 예외처리
        if not matrix:
            return False
        
        # 첫 행의 맨 뒤 비교
        row = 0
        col = len(matrix[0]) - 1
        
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True

            # target is smaller
            elif target < matrix[row][col]:
                col -= 1
            # target is bigger
            elif target > matrix[row][col]:
                row += 1
        return False