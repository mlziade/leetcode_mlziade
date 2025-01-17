from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.iterateList(head, None, 0)
        return head
        
    def iterateList(self, node: ListNode, last_zero: ListNode, sum: int):
        if not node:
            return
        
        elif node.val == 0 and last_zero == None:
            self.iterateList(node.next, node, sum)
        
        elif node.val == 0 and last_zero != None:
            last_zero.val = sum
            last_zero.next = node.next
            self.iterateList(node.next, last_zero.next, 0)
        
        else:
            self.iterateList(node.next, last_zero, sum + node.val)