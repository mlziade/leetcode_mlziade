# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def calculateDepth(node: TreeNode) -> int:
    if node is None:
            return 0
    else:
        left = calculateDepth(node.left)
        right = calculateDepth(node.right)
        return right + 1 if right > left else left + 1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return calculateDepth(root)