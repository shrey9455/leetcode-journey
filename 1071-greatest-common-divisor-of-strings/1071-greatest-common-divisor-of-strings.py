class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        result=""
        for i in range(len(str2)):
            sub = str2[:i+1]

            if (len(str1) % len(sub) == 0 and
                len(str2) % len(sub) == 0 and
                str1 == sub * (len(str1)//len(sub)) and
                str2 == sub * (len(str2)//len(sub))):
                
                result = sub

        return result