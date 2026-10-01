class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair={")":"(","}":"{","]":"["}
        stack=[] 
        for i in s:
            if i in pair:
                if stack and pair[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return  False if stack else True