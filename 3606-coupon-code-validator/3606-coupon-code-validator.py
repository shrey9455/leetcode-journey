class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        check = ["electronics", "grocery", "pharmacy", "restaurant"]
        result = []

        for i in range(len(code)):
            if isActive[i] and businessLine[i] in check and code[i] != "":
                valid = True

                for j in code[i]:
                    if not j.isdigit() and j != "_" and not j.isalnum():
                        valid = False
                        break

                if valid:
                    result.append((check.index(businessLine[i]), code[i]))

        result.sort()

        return [x[1] for x in result]