class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        even=[i for i in nums1 if i%2==0]
        odd=[i for i in nums1 if i%2!=0]
        if len(even):
            return True
        if len(odd):
            return True
        return False