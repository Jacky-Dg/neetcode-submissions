class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht = {}

        l = 0
        cl = ""
        for c in s:
            if ht.get(c):
                if len(cl) > l:
                    l = len(cl)
                cl = cl[1:]

                if cl:
                    if c != cl[0]:
                        cl += c
                else:
                    cl += c
            else:
                cl += c
                ht[c] = 1
        
        print(cl)
        return l if l > len(cl) else len(cl)
