class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        dict = {}
        summ_arr = []
        compare_arr = []

        for i in nums:
            digit_sum = sum(int(digit) for digit in str(i))

            if digit_sum in dict:
                dict[digit_sum].append(i)
            else:
                dict[digit_sum] = [i]

            summ_arr.append(digit_sum)

        summ_arr = sorted(set(summ_arr))

        for i in summ_arr:
            compare_arr.extend(sorted(dict[i]))

        index_map = {num: i for i, num in enumerate(compare_arr)}
        seen = set()

        for i in range(len(nums)):
            if i in seen or index_map[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while j not in seen:
                seen.add(j)
                j = index_map[nums[j]]
                cycle_size += 1

            result += cycle_size - 1

        return result