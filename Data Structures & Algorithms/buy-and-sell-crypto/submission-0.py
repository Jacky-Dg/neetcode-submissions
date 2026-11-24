class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high_id = 0
        low_id = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
                low_id = i
        
        highest = 0
        for i in range(low_id, len(prices)):
            if prices[i] > highest:
                highest = prices[i]
                high_id = i

        if high_id < low_id:
            return 0
        else:
            return highest - lowest
                