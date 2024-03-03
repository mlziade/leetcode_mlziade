# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0, None)
        aux1 = l1
        aux2 = l2
        aux3 = l3
        vai1 = False
        while (aux1 or aux2):
            if aux1:
                aux3.val += aux1.val
            if aux2:
                aux3.val += aux2.val
            if vai1 == True: #Verifica se tem mais 1 da ultima iteracao
                aux3.val += 1
                vai1 = False
            if aux3.val > 9: #Verifica se tem mais 1 na proxima iteracao
                aux3.val = aux3.val % 10
                vai1 = True
            print(aux1, aux2, aux3, vai1, sep="\n")
            if aux1: #Avança aux1 se não for None
                aux1 = aux1.next
            if aux2: #Avança aux2 se não for None
                aux2 = aux2.next
            if aux1 or aux2:
                aux3.next = ListNode(0,None)
            if not aux1 and not aux2 and vai1 == True:
                aux3.next = ListNode(1,None)
            aux3 = aux3.next
            print("-------------------")
        return l3

            