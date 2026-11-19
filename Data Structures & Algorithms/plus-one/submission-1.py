class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0

        for digit in digits:
            number *= 10
            number += digit

        number += 1

        return [int(digit) for digit in str(number)]