class Solution:
    def isHappy(self, n: int) -> bool:
        nString = str(n)
        seen = []

        total = 0
        while total not in seen and total != 1:
            total = 0
            for c in nString:
                total += int(c) ** 2

            seen.append(total)
            nString = str(total)

        return total == 1
