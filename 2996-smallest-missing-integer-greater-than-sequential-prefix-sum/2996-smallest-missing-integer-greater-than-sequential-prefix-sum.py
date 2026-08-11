class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen =set(nums)
        summ=0
        cur_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                cur_sum+=nums[i]
            else:
                break
        while cur_sum in seen:
            cur_sum += 1

        return cur_sum