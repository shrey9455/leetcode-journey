class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge=sorted(nums1+nums2)

        if len(merge)%2==0:
            result=float(merge[len(merge)//2]+merge[len(merge)//2-1])/2.0
        else:
            result=merge[len(merge)//2]
        return result