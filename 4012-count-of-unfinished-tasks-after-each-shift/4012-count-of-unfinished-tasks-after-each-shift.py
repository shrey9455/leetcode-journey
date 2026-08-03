class Solution(object):
    def countTasks(self, tasks, shifts):
        """
        :type tasks: List[int]
        :type shifts: List[int]
        :rtype: List[int]
        """
        m = len(tasks)
        n = len(shifts)

        prefix = [0] * m
        prefix[0] = tasks[0]
        for i in range(1, m):
            prefix[i] = prefix[i-1] + tasks[i]

        total = sum(tasks)

        cur = 0
        ans = []
        for e in shifts:
            cur += e
            if cur >= total:
                ans.append(0)
                cur = 0
            else:
                completed = bisect_right(prefix, cur)
                ans.append(m-completed)

        return ans
        