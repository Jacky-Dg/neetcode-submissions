class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        biggest_pile = 0
        bananas = 0
        for pile in piles:
            bananas += pile
            if pile > biggest_pile:
                biggest_pile = pile
        
        if h > len(piles):
            return (bananas // h) + 1
        else:
            return biggest_pile