class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        cur=0
        for i in s:
            if i == "(":
                cur += 1
                result = max(result, cur)
            elif i == ")":
                cur -= 1
        return result