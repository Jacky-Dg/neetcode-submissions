class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}

        l = r = 0
        max = 0
        for c in s:
            if ht.get(c):
                l += 1
                curr_max = r - l + 1

                if curr_max > max:
                    max = curr_max
            else:
                ht[c] = 1
                r += 1
        
        
        return max
