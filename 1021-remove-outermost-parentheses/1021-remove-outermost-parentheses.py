class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        open=0
        close=0
        for i in s:
            if i=="(":
                open+=1
            else:
                close+=1
            
            if open==close:
                open=0
                close=0
            elif open>close:
                if open>1:
                    stack.append(i)
            else:
                open=0
                close=0
            
        return "".join(stack)