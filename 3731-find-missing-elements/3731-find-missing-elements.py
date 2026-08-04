class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(min(nums),max(nums)):
            if i+1 not in nums:
                result.append(i+1)
        return result