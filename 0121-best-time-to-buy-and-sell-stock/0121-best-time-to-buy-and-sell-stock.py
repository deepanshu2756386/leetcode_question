class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            min_p = min(min_p  , prices[i])

            profit = prices[i] - min_p

            max_profit = max(profit , max_profit)


        return max_profit 
         


        