class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()[::-1]
        result=""
        for i in s:
            if result=="":
                result+=i
            else:
                result=result+" "+i
        return result