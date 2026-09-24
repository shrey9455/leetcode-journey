class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=float('inf')
        for i in range(len(nums)):
            summ=0
            for j in str(nums[i]):
                summ+=int(j)
            if summ==i:
                result=min(result,i)
        return -1 if result==float('inf') else result