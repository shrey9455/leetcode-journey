class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sub=nums[i:j+1]
                result+=(len(set(sub))**2)
        return result