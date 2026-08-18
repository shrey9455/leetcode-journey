class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sub=float('inf')
        result=-1
        seen=set()
        for i in range(len(nums)):
            m=0
            cur_sub=0
            if nums[i] in seen:
                continue
            while m+k<=len(nums) :
                if nums[i] in nums[m:m+k]:
                    cur_sub+=1
                m+=1
            if cur_sub == 1:
                result = max(result, nums[i])   
            # if sub==float('inf'):
            #     sub=cur_sub
            #     if cur_sub==1:
            #         result=nums[i]
            # elif sub==cur_sub:
            #     if cur_sub==1 and nums[i]>result:
            #         result=nums[i]
            # elif sub>cur_sub:
            #     sub=cur_sub
            #     result=nums[i]

            seen.add(nums[i])

        return result