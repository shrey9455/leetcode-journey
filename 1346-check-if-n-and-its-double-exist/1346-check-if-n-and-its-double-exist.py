class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # seen=set()
        
        for i in range(len(arr)):
            if 2*arr[i] in arr[:i]+arr[i+1:]:
                return True
        else:
            return False