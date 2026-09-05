class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        mn=float('inf')
        suffix=[0]*n
        for i in range(n-1,-1,-1):
            mn=min(mn,nums[i])
            suffix[i]=mn
        mx=0
        for i in range(n):
            mx=max(mx,nums[i])
            if mx-suffix[i]<=k:
                return i

        return -1