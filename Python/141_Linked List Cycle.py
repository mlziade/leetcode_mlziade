# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        aux = head
        nodes = {}
        while(True):
            if aux == None: return False
            adress = hex(id(aux))
            if adress in nodes: return True
            nodes[adress] = aux
            aux = aux.next