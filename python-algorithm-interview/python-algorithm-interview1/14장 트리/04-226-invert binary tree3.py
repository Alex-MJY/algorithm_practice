# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs (하향식)

class Solution:
    def invertTree(self, root: TreeNode):
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
            
                stack.append(node.left)
                stack.append(node.right)

        return root
    
an = Solution()
root = [4,2,7,1,3,6,9]
print(an.invertTree(root))