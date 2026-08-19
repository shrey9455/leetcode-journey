class Solution(object):
    def strStr(self, haystack, needle):
        j=0
        i=0
        k=0
        while i<len(haystack) :
            if j<len(needle) and haystack[i]==needle[j]:
                j+=1
                i+=1
            elif j==len(needle):
                return k
            else:
                j=0
                k+=1
                i=k
        if j==len(needle):
            return k
        return -1