class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) % 2 != 0):
            return False
        
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for c in s:
            if c in bracket_map.values():
                stack.append(c)
            else:
                if not stack or bracket_map[c] != stack[-1]:
                    return False
                stack.pop()
            
        return len(stack) == 0