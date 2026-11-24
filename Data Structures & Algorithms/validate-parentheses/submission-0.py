class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) % 2 != 0):
            return False
        
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        values = bracket_map.values()

        for i in range(int(len(s) / 2)):
            if (s[i] not in values) or (s[i] != bracket_map[s[(len(s) - i - 1)]]):
                return False

        return True