# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        arr=[]
        cur=head
        prev=cur
        index=1
        while cur and cur.next:
            
            if cur.next is not None:
                nxt=cur.next
            else:
                break
            if prev!=cur:
                if prev.val>cur.val<nxt.val or prev.val<cur.val>nxt.val:
                    arr.append(index)
            prev=cur
            cur=cur.next
            index+=1
        arr=sorted(arr,reverse=True)
        if len(arr)<2:
            return [-1,-1]
        minimum = float('inf')

        for i in range(1, len(arr)):
            minimum = min(minimum, abs(arr[i] - arr[i - 1]))

        maximum = arr[0]- arr[-1]

        return [minimum, maximum]