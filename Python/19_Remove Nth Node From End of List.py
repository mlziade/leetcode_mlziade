# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        aux_node = head #Aux_node references the same object as head
        counter = 0
        target = -1
        find_last_node(aux_node, 0)
        return head

def find_last_node(node, counter):
    if node.next == None: #Ao final da lista
        target = counter - n + 1 # Calcula qual posicao da lista que deve ser removido
        return None
    if counter == target: #Se o nodo atual é o nodo a ser removido
        return node.next
    print(counter)
    aux = find_last_node(node.next, counter + 1)
    if aux != None:
        node.next = aux




