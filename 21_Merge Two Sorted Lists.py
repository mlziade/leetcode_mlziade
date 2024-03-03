# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if not list1 and not list2:
            return None
        list3 = aux3 = ListNode()
        aux1, aux2= list1, list2
        while aux1 and aux2:
            print(aux1, aux2, list3)
            if aux1.val <= aux2.val:
                aux3.next = ListNode(aux1.val, None)
                aux3 = aux3.next
                aux1 = aux1.next
                if aux1 == None:
                    aux3.next = aux2
            elif aux2.val < aux1.val:
                aux3.next = ListNode(aux2.val, None)
                aux3 = aux3.next
                aux2 = aux2.next
                if aux2 == None:
                    aux3.next = aux1
        return list3.next