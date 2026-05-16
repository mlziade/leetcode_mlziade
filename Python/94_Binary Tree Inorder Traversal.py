# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        array = []

        if root == None:
            return []
        
        if root.left != None:
            array.extend(
                self.inorderTraversal(root.left)
            )

        array.append(root.val)
        
        if root.right != None:
            array.extend(
                self.inorderTraversal(root.right)
            )
        
        return array
