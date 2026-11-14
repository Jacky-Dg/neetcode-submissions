class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Iterate through array with index i
        # i is the sell value
        # the buy value is the smallest value to the left of i
        # keep track of profits, if no increase or decrease then dont change values
        buy_value = prices[0]
        buy_id = 0
        curr_profit = 0

        for i in range(1, len(prices)):
            if buy_value < prices[i]:
                new_profit = prices[i] - buy_value
                if new_profit > curr_profit:
                    curr_profit = new_profit
                    low_id = i
            
            if buy_value > prices[i] and i != len(prices) - 1:
                buy_value = prices[i]
                buy_id = i

        return curr_profit
                
                