'''1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라'''

# dfs로 그래프 탐색
# 네 방향 각각 dfs 재귀를 이용해 탐색을 끝마치면 1이 증가하는 형태로 육지의 개수를 파악할 수 있다.
# 행렬(matrix) 입력값인 rows, cols 단위로 육지(1)인 곳을 찾아 진행하다가 육지를 발견하면, 그때부터 self.dfs()를 호출해 탐색 시작.
# 이미 방문한 값은 1이 아닌 값으로 마킹한다.
class Solution:
    def numIslands(self, grid: list) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return
            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count