class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapp={}
        for i in range(len(s)):
            if s[i] not in mapp:
                if t[i] in mapp.values():
                    return False
                    break
                else:
                    mapp[s[i]]=t[i]
            else:
                if mapp[s[i]]!=t[i]:
                    return False
                    break
        else:
            return True
            