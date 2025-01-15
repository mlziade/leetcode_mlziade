# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def go_through_tree(p: TreeNode, q: TreeNode):
    if p is None and q is None:
        return True
    if (p is None and q) or (p and q is None):
        return False
    elif p.val == q.val:
        left = go_through_tree(p.left, q.left)
        if not left:
            return False
        right = go_through_tree(p.right, q.right)
        if not right:
            return False
        return True
    else:
        return False

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return go_through_tree(p, q)
    

## Better solution
    
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)