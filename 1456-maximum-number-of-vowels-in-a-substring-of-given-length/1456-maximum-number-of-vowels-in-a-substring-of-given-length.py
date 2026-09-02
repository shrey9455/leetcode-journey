class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count=0

        for i in s[:k]:
            if i in ['a', 'e', 'i', 'o','u']:
                count+=1
        result=count
        left=0
        for i in range(k,len(s)):
            if s[left] in ['a', 'e', 'i', 'o','u']:
                count-=1
            if s[i] in ['a', 'e', 'i', 'o','u']:
                count+=1
            left+=1
            result=max(result,count)
        return result