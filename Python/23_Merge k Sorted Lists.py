# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        cursor = response = ListNode()
        while(True):
            smallest = returnSmallestItem(lists)
            if lists.count(None) == len(lists) - 1:
                cursor.next = lists[smallest]
                return response.next
            if smallest == -1:
                return response.next
            cursor.next = ListNode(lists[smallest].val, None)
            cursor = cursor.next
            lists[smallest] = lists[smallest].next
            if lists[smallest] == None:
                lists.remove(None) 
        return response

def returnSmallestItem(lists):
    #print(lists)
    index = -1
    val = pow(10,4) + 1
    for i in range (len(lists)):
        if lists[i] != None:
            if lists[i].val < val:
                index = i
                val = lists[i].val
    #print(index)
    return index 