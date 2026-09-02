class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        result=float('-inf')
        while i<j:
            result=max(min(height[i],height[j])*(j-i),result)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return result