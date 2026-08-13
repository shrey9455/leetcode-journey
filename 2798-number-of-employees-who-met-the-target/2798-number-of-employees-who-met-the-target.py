class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        result=0
        for i in hours:
            if i>=target:
                result+=1
        return result