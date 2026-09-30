class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        r=[0]*len(seq)
        depth=0
        for i in range(len(seq)):
            if seq[i]=="(":
                depth+=1
                r[i]=(depth %2)
                continue
            r[i]=(depth %2)
            depth-=1
        return r