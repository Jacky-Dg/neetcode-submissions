class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number *= 10
            number += digit
        number += 1

        def to_char_array(s: str) -> list[str]:
            return list(s)

        return to_char_array(str(number))