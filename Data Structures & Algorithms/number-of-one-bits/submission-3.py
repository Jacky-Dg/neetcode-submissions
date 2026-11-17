class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        bits = len(bin(n)[2:])

        for i in range(bits):
            if n & (1 << i):
                count += 1
        
        return count