class Solution(object):
    def productExceptSelf(self, nums):
        result=[1]*len(nums)
        for i in range(1,len(nums)):
            result[i]=result[i-1]*nums[i-1]
        right=1
        for j in range(len(nums)-1,-1,-1):
            result[j]=right*result[j]
            right=right*nums[j]
        return result