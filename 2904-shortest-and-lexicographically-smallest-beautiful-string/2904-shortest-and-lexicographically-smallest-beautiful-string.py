class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left=0
        result=""
        right=0
        count=0
        while right < len(s):
            if s[right]=='1':
                count+=1

            while count==k:
                sub=s[left:right+1]

                if result=="":
                    result=sub
                elif len(result)==len(sub):
                    result=min(result, sub)
                elif len(result)>len(sub):
                    result=sub

                if s[left]=='1':
                    count-=1
                left+=1

            right+=1
        return result