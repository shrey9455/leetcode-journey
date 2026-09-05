class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occurence=[]
        count=Counter(arr)
        for i in count:
            occurence.append(count[i])
        unique=set()
        for i in occurence:
            if i not in unique:
                unique.add(i)
            else:
                return False
        return True