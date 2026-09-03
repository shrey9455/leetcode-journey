class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(0)==0:
            return len(nums)-1
        i=0
        count=0
        result=0
        for j in range(len(nums)):
            if nums[j]==0:
                count+=1
            while count>1:
                if nums[i]==0:
                    count-=1
                i+=1
            result=max(j-i,result)
        return result