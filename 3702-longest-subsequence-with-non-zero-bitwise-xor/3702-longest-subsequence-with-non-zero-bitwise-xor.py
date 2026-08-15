class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total =0
        non_zero=False
        for i in nums:
            total^=i
            if i!=0:
                non_zero=True
        if total!=0:
            return len(nums)
        if non_zero:
            return len(nums)-1
        else:
            return 0