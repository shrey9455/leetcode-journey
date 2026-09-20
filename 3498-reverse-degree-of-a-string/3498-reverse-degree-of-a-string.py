class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        degree="abcdefghijklmnopqrstuvwxyz"
        degree=degree[::-1]
        result=0
        index=1
        for i in s:
            result+=(index*(degree.index(i)+1))
            index+=1
        return result