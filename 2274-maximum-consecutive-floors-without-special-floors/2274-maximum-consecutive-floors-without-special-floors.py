class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        result=0
        floor=0
        special.sort()
        for i in range(len(special)):
            floor=(special[i]-1)-bottom+1
            bottom=special[i]+1
            result=max(result,floor)
        result=max(result,top-(special[i]+1)+1 )
        return result