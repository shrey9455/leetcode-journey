class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        ans=0
        freq=[0]*10
        for i in digits:
            freq[i]+=1
        for first in range(1,10):
            if freq[first]==0:
                continue
            freq[first]-=1
            for second in range(10):
                if freq[second]==0:
                    continue
                freq[second]-=1
                for last in range(0,10,2):
                    if freq[last]>0:
                        ans+=1
                freq[second]+=1
            freq[first]+=1
        return ans