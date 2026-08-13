class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        summ=0
        for i in nums:
            summ+=i
            result.append(summ)
        return result