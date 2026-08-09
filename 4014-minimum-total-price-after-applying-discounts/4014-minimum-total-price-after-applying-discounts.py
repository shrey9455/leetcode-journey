class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
        prices=sorted(prices,reverse=True)
        discounts=sorted(discounts,reverse=True)
        result=0.0
        for i in range(len(prices)):
            if i<len(discounts):
                result+=prices[i]*(100-discounts[i])/100.0
            else:
                result+=prices[i]
        return result