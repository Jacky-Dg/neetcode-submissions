class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = len(s)
        if(l <= 1):
            return True

        for i in range(int(l/2)):
            if not s[i] == s[l - i - 1]:
                return False

        return True