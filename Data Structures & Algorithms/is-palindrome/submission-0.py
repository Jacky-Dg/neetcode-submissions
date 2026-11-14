class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum()).lower()
        l = len(clean)

        for i in range(int(l/2)):
            if clean[i] != clean[l-1-i]:
                return False;

        return True;
