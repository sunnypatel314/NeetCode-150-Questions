from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            node = cur.next
            cur.next = prev
            prev = cur
            cur = node
        return prev

solution = Solution()

print(solution.reverseList(head = [0,1,2,3])) # [3,2,1,0]
print(solution.reverseList(head= [])) # [] 
