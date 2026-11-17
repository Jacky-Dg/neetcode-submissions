class Solution:
    def isHappy(self, n: int) -> bool:
        nString = str(n)
        seen = {}

        total = 0
        while seen.get(nString) != 1 and total != 1:
            total = 0
            for c in nString:
                total += int(c) ** 2

            seen[nString] = 1
            nString = str(total)

        return total == 1
