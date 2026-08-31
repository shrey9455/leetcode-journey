class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        if len(nums)<3:
            return len(nums)
        def front(max_index,min_index):
            return max(min_index,max_index)+1
        def back(nums,max_index,min_index):
            return len(nums)-min(max_index,min_index)
        def both(nums,max_index,min_index):
            left = min(max_index, min_index)
            right = max(max_index, min_index)
            return (left + 1) + (len(nums) - right)
            # mid=len(nums)//2-1
            # if mid<max_index and mid<min_index:
            #     return len(nums)-(min(max_index,min_index))
            # elif mid>max_index and mid>min_index:
            #     return max(max_index,min_index)+1
            # elif mid>max_index and mid<min_index:
            #     return (max_index+1)+(len(nums)-min_index)
            # elif mid>min_index and mid<max_index:
            #     return (min_index+1)+(len(nums)-max_index)
        maximum=nums[0]
        minimum=nums[0]
        max_index=0
        min_index=0
        for i in range(1,len(nums)):
            if maximum<nums[i]:
                maximum=nums[i]
                max_index=i
            if minimum>nums[i]:
                minimum=nums[i]
                min_index=i
        return min(front(max_index,min_index),back(nums,max_index,min_index),both(nums,max_index,min_index))