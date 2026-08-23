class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        left_sum = 0
        right_sum = 0
        left_count = 0
        right_count = 0

        for i in range(n):
            if num[i] == '?':
                if i < n // 2:
                    left_count += 1
                else:
                    right_count += 1
            else:
                if i < n // 2:
                    left_sum += int(num[i])
                else:
                    right_sum += int(num[i])

        if (left_count + right_count) % 2 == 1:
            return True

        diff_count = left_count - right_count
        diff_sum = left_sum - right_sum

        return diff_sum != -9 * (diff_count // 2)