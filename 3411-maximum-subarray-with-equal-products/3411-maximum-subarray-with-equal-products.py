class Solution:
    def maxLength(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            prod = 1
            arr = []

            for j in range(i, len(nums)):
                prod *= nums[j]
                arr.append(nums[j])

                arr_lcm = math.lcm(*arr)
                arr_gcd = math.gcd(*arr)

                if prod == arr_gcd * arr_lcm:
                    result = max(result, len(arr))
        return result