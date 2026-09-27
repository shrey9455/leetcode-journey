class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = ""
        stack = []
        for i in s:
            if i == "(":
                stack.append(string)
                string = ""

            elif i == ")":
                string = stack.pop() + string[::-1]

            else:
                string += i
        return string