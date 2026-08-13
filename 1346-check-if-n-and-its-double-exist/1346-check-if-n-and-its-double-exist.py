class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # seen=set()
        
        for i in range(len(arr)):
            sub=arr[:i]+arr[i+1:]
            if 2*arr[i] in sub:
                return True
        else:
            return False