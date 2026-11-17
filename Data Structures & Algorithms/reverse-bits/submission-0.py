class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0

        for i in range(32):
            if (n >> i) & 1:
                output |= (1 << (31-i))
        
        return output

        
