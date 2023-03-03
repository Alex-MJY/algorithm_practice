# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# DFS, Bruteforce

# dfs로 전체를 탐색한 다음, 노드의 값이 low와 high의 사이일 때만 값을 부여하고, 아닌 경우에는 0을 취해 계속 더해 나간다.
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        
        return (root.val if low <= root.val <= high else 0) + \
            self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)