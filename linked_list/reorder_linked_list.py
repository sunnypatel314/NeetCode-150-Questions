from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next, prev = None, None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        first, second = head, prev
        while second:
            first_temp, second_temp = first.next, second.next
            first.next = second
            second.next = first_temp
            first = first_temp
            second = second_temp

        
solution = Solution()

print(solution.reorderList(head = [2,4,6,8])) # [2,8,4,6]
print(solution.reorderList(head = [2,4,6,8,10])) # [2,10,4,8,6]
    

