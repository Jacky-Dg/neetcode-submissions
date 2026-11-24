class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}

        l = 0
        cl = 0
        for c in s:
            if ht.get(c):
                if cl > l:
                    l = cl
                cl = 1
                ht = {c: 1}
            else:
                cl += 1
                ht[c] = 1
        
        return l if l > cl else cl
