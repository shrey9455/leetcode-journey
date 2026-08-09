# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = head
        arr = []

        while cur:
            arr.append(cur.val)
            cur = cur.next

        result = []
        maximum = float('-inf')

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= maximum:
                result.append(arr[i])
                maximum = arr[i]

        result.reverse()

        dummy = ListNode(0)
        h = dummy

        for x in result:
            h.next = ListNode(x)
            h = h.next

        return dummy.next
            