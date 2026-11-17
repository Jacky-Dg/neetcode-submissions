class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        binrep = bin(n)[2:]

        for bit in binrep:
            if bit == '1':
                count = count + 1

        return count