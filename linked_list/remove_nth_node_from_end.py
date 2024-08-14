from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = head
        while dummy:
            count += 1
            dummy = dummy.next
        
        n = count - n + 1

        if count == 1:
            return None
        if n == 1:
            return head.next

        dummy = head
        while dummy:
            if n == 2:
                dummy.next = dummy.next.next
                break
            dummy = dummy.next
            n -= 1
        return head
        

solution = Solution()
print(solution.removeNthFromEnd(head = [1,2,3,4], n = 2)) # [1,2,4]
print(solution.removeNthFromEnd(head = [5], n = 1)) # []
print(solution.removeNthFromEnd(head = [1,2], n = 2)) # [2]



