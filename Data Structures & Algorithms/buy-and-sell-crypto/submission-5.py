class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_value = prices[0]
        curr_profit = 0

        for i in range(1, len(prices)):
            if buy_value < prices[i]:
                new_profit = prices[i] - buy_value
                if new_profit > curr_profit:
                    curr_profit = new_profit
                    low_id = i
            
            if buy_value > prices[i] and i != len(prices) - 1:
                buy_value = prices[i]

        return curr_profit
                
                