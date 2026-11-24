class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        return (1 + climbStairs(n - 1) + climbStairs(n - 2))

