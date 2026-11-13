class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        
        hash_s = {};
        hash_t = {};

        for c in s:
            if not hash_s.get(c):
                hash_s[c] = 1;
            else:
                hash_s[c] = hash_s[c] + 1; 

        for c in t:
            if not hash_t.get(c):
                hash_t[c] = 1;
            else:
                hash_t[c] = hash_t[c] + 1;

        for c in hash_s:
            if (not hash_t.get(c)) or hash_s[c] != hash_t[c]:
                return False;

        return True;
