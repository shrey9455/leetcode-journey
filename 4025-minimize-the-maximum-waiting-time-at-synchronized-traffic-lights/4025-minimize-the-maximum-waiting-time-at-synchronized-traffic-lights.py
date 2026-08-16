class Solution(object):
    def minPenalty(self, period, lights, arrivalTime):
        """
        :type period: int
        :type lights: List[int]
        :type arrivalTime: List[int]
        :rtype: int
        """
        result = 0
        max_light=max(lights)
        for i in arrivalTime:
            r=i %period
            if r>=max_light:
                result=max(result,period-r)
        return result