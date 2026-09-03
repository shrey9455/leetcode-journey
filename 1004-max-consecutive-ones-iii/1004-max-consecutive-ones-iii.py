class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count_of_one=0
        count_of_zero=0
        result=float('-inf')
        i=0
        for j in range(len(nums)):
            if nums[j]==0:
                count_of_zero+=1
            else:
                count_of_one+=1
            if count_of_zero<=k:
                result=max(count_of_zero+count_of_one,result)
            else:
                while count_of_zero>k:
                    if nums[i]==0:
                        count_of_zero-=1
                    else:
                        count_of_one-=1
                    i+=1
            
                result=max(count_of_zero+count_of_one,result)
        return result