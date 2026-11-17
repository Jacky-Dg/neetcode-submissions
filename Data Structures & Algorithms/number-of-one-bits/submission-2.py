class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        bits = 32

        for i in range(bits):
            if n & (1 << i):
                count += 1
        
        return count