# 203. Remove Linked List Elements
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

                return dummy.next
