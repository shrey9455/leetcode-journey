class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        summ=0
        prod=1
        for i in str(n):
            summ+=int(i)
            prod*=int(i)
        if n%(summ+prod)==0:
            return True
        else:
            return False