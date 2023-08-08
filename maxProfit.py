class Solution:
    def maxProfit(self, prices: List[int]) -> int:             
        minPrice = 10**4
        maxProfit = 0
        
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            
            profitToday = prices[i] - minPrice

            if profitToday > maxProfit:
                maxProfit = profitToday
        
        return maxProfit
