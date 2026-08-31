class Solution(object):
    def sumDecoded(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        mod=(10**9)+7
        for i in nums:
            width = i % 10
            d=str(i//10)
            x=int(d[:width])
            y=int(d[width:])
            result=(result+pow(x,y,mod))%mod
        return result