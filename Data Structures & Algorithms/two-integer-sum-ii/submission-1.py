class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers) - 1

        while l < h - 1:
            m = (l + h) // 2

            if numbers[l] + numbers[m] == target:
                h = m 
                break
            elif numbers[m] + numbers[h] == target:
                l = m
                break
            elif numbers[l] + numbers[m] < target:
                l = m
            else: 
                h = m

        return [numbers[l], numbers[h]]

