class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}
        l = m = 0

        for r in range(len(s)):
            while s[r] in ht:
                del ht[s[l]]
                l += 1

            ht[s[r]] = 1
            m = max(m, r - l + 1)

        return m