class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        x={i[0]:i[1] for i in knowledge}
        result=""
        check=False
        bracket=""
        for i in s:
            if i=="(":
                check=True
                continue
            if check:
                if i!=")":
                    bracket+=i
                else:
                    check=False
                    result += x.get(bracket, "?")
                    bracket=""
            else:
                result+=i
        return result