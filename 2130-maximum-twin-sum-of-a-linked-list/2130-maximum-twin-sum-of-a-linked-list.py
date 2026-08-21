# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        stack=[]
        cur=head
        count=0
        while cur:
            stack.append(cur.val)
            cur=cur.next
            count+=1
        result=0
        index=0
        while index!=count//2 and head:
            twim=head.val+stack.pop()
            result=max(result,twim)
            head=head.next
            index+=1
        return result