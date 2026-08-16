class Solution(object):
    def maximumGap(self, skill, station):
        """
        :type skill: str
        :type station: str
        :rtype: int
        """
        left = []
        right = []


        j = 0

        for i in range(len(skill)):
            while j < len(station):
                if skill[i] == station[j]:
                    left.append(j)
                    j += 1
                    break
                j += 1

        # Find latest possible positions
        j = len(station) - 1

        for i in range(len(skill) - 1, -1, -1):
            while j >= 0:
                if skill[i] == station[j]:
                    right.append(j)
                    j -= 1
                    break
                j -= 1

        right = right[::-1]

        result = 0

        i = 1
        while i < len(left):
            result = max(result, right[i] - left[i-1])
            i += 1

        return result