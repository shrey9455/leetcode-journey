class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def check(n):
            prod=1
            while n>0:
                digit=n%10
                n=n//10
                prod*=digit
                if prod==0:
                    break
            return prod%t==0
        while not check(n):
            n+=1
        return n