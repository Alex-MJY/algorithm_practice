# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs (하향식, 전위순회, pre order)

class Solution:
    def invertTree(self, root: TreeNode):
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
            
                queue.append(node.left)
                queue.append(node.right)

        return root
    
an = Solution()
root = [4,2,7,1,3,6,9]
print(an.invertTree(root))