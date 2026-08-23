class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary=bin(n)[2:].zfill(32)
        return int(binary[::-1],2)