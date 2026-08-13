class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        container=0
        result=0
        while i<j:
            container=min(height[i],height[j])*(j-i)
            result=max(result,container)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return result