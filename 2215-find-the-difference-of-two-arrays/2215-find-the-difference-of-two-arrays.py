class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        hash1=set()
        hash2=set()
        for i in nums1:
            if i not in nums2:
                hash1.add(i)
        ans.append(list(hash1))
        for i in nums2:
            if i not in nums1:
                hash2.add(i)
        ans.append(list(hash2))
        return ans