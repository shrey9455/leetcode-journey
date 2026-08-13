class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        n=len(nums)
        ans=[]
        for i in range(2*n):
            if i>=n:
                ans.append(nums[i-n])
            else:
                ans.append(nums[i])
        return ans