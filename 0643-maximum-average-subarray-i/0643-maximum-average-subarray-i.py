class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window = float(sum(nums[:k]))
        result = window / k

        for i in range(k, len(nums)):
            window -= nums[i-k]
            window += nums[i]
            result = max(result, window / k)

        return result