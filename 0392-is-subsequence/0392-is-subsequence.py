class Solution(object):
    def isSubsequence(self, s, t):
        i=j=0
        if len(s)==0:
            return True
        
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                if i==len(s)-1 and s[i]==t[j]:
                    return True
                i+=1
                j+=1
            else:
                j+=1

        else:
            return False