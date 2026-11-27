# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, m, r = 0, n // 2, n

        while guess(m) != 0:
            if guess(m) < 0:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2

        return m

