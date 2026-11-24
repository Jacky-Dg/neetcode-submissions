class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}

        l = 0
        cl = ""
        remove = ""
        for c in s:
            if ht.get(c):
                if len(cl) > l:
                    l = len(cl)
                if cl:
                    removed = cl[0]
                cl = cl[1:]

                if cl:
                    if c != cl[0] and c != removed:
                        cl += c
                else:
                    cl += c
            else:
                cl += c
                ht[c] = 1
        
        return l if l > len(cl) else len(cl)
