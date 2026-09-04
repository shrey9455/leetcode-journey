class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt=0
        mx=0
        for i in gain:
            alt+=i
            mx=max(mx,alt)
        return mx
