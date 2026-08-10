# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        index = 0
        cur = head

        while cur:
            index += 1
            cur = cur.next

        mid = index//2+1

        index = 1
        dummy = ListNode(0)
        cur = dummy

        while head:
            if mid == index:
                head = head.next
            else:
                cur.next = head
                cur = cur.next
                head = head.next

            index += 1
        cur.next=None

        return dummy.next