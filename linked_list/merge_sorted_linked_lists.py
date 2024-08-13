from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
            
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        node.next = list1 or list2

        return dummy.next

solution = Solution()

print(solution.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,5])) # [1,1,2,3,4,5]
print(solution.mergeTwoLists(list1 = [], list2 = [1,2])) # [1,2]
print(solution.mergeTwoLists(list1 = [], list2 = [])) # []
