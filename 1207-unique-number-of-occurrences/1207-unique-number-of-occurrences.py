class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count=Counter(arr)
        unique=set()
        for i in count:
            if count[i] not in unique:
                unique.add(count[i])
            else:
                return False
        return True