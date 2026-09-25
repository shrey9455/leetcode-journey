class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums1[i] == nums2[j]:
                result.append(nums1[i])
                result.append(nums2[j])
                i += 1
                j += 1
            else:
                result.append(nums2[j])
                j += 1

        if j < n:
            result.extend(nums2[j:])

        if i < m:
            result.extend(nums1[i:m])

        nums1[:] = result