class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1

        if n <= 2:
            return n
        for i in range(2, n):
            second += first
            first += second

        return first
