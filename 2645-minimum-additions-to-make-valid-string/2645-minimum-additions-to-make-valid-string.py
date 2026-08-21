class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        stack=[]
        expected=97
        count=0
        for i in word:
            cur=ord(i)
            while expected!=cur:
                stack.append(chr(expected))
                expected=expected+1
                if expected==100:
                    expected=97
                count+=1
            else:
                stack.append(chr(expected))
                expected=expected+1
                if expected==100:
                    expected=97
        if expected == 97:
            count += 0
        elif expected == 98:
            count += 2
        elif expected == 99:
            count += 1
        return count