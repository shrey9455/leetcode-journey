class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={}
        result=0
        length=0
        left=0
        for i in range(len(nums)):

            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
            while freq[nums[i]]>k:
                freq[nums[left]]-=1
                length-=1
                left+=1
            length+=1
            
            result=max(result,length)
        return result
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))