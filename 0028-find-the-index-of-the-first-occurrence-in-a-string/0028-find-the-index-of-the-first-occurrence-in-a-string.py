class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            j=0
            while j<len(needle):
                if i+j<len(haystack) and haystack[i+j]==needle[j]:
                    j+=1
                else:
                    break
            else:
                return i
        return -1