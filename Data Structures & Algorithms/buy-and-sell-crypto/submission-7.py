class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_value = prices[0]
        curr_profit = 0

        for i in range(1, len(prices)):
            sell_value = prices[i]
            if buy_value < sell_value:
                new_profit = sell_value - buy_value
                if new_profit > curr_profit:
                    curr_profit = new_profit
            
            if buy_value > sell_value and i != len(prices) - 1:
                buy_value = sell_value

        return curr_profit
                
                