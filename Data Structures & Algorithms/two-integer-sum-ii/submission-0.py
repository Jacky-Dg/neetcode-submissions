class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1

        while low < high - 1:
            mid = (low + high) // 2

            if low + mid == target:
                return [low, mid]
            elif mid + high == target:
                return [mid, high]
            elif low + mid < target:
                low = mid
            else: 
                high = mid

        return [low, high]

