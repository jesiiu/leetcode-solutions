#2. Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry

        carry, remainder = divmod(total, 10)
        current.next = ListNode(remainder)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        return dummy_head.next
            