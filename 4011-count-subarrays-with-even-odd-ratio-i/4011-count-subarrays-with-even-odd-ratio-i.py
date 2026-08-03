class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:


        result = 0
        length = len(nums)
        
        for i in range(length):

            even , odd = 0 , 0

            for j in range(i, length):

                if nums[j] % 2 == 0:
                    even = even + 1
                else:
                    odd = odd + 1

                if odd > 0:

                    if (even / odd) <= (a / b):
                        result = result + 1
                
        return result