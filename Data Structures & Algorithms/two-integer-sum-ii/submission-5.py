class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, h = 0, len(numbers) - 1

        while l < h - 1 and (numbers[l] + numbers[h] != target):
            m = (l + h) // 2

            if numbers[l] + numbers[m] == target:
                h = m 
                break
            elif numbers[m] + numbers[h] == target:
                l = l
                break
            elif numbers[l] + numbers[m] < target:
                l = l + 1
            else: 
                h = h + 1

        return [l + 1, h + 1]

