class Solution:
    def isHappy(self, n: int) -> bool:
        nString = str(n)
        seen = set()

        total = 0
        while nString not in seen and total != 1:
            total = 0
            for c in nString:
                total += int(c) ** 2

            seen.add(nString)
            nString = str(total)

        return total == 1
