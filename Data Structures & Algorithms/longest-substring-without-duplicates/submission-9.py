class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}

        l = r = 0
        m = 0
        for i in range(len(s)):
            if ht.get(s[i]):
                l += 1
                curr_max = r - l + 1

                if curr_max > m:
                    m = curr_max
            else:
                ht[s[i]] = 1
                r += 1
        
        
        return max(m, r - l)
