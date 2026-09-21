class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        mapping = set()

        for x, y in mappings:
            mapping.add((x, y))

        for i in range(len(s) - len(sub) + 1):
            found_all = True

            for j in range(len(sub)):

                if s[i + j] == sub[j]:
                    continue

                if (sub[j], s[i + j]) not in mapping:
                    found_all = False
                    break

            if found_all:
                return True

        return False