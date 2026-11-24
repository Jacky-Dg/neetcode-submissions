class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1

        if n <= 2:
            return n
        for i in range(n - 2):
            second += first
            first += second

        return first
