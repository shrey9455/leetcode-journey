class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        string=""
        for i in s:
            if i==']':
                decode=""
                while stack[-1]!='[':
                    decode=stack.pop()+decode
                # decode=decode[::-1]
                stack.pop()
                repeat=""
                while stack and stack[-1].isdigit():
                    repeat=stack.pop()+repeat
                stack.append(int(repeat)*decode)
            else:
                stack.append(i)
                    
        return "".join(stack)