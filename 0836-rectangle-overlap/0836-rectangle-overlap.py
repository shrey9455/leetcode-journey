class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1,y1,x2,y2=rec1
        X1,Y1,X2,Y2=rec2
        return x1<X2 and y1<Y2 and X1<x2 and Y1<y2