class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        plant=0
        count=1
        for i in flowerbed:
            if i==0:
                count+=1
            else:
                plant+=(count-1)//2
                count=0
        return plant+count//2>=n