class Solution(object):
    def containsDuplicate(self, nums):
        dupl=set()
        for n in nums:
            if n in dupl:
                return True
            dupl.add(n)
        return False