class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        left = 0
        right = len(nums) - 1
        if target == nums[left]:
            return left
        if target == nums[right]:
            return right

        while(1):
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid
            else:
                return mid
        
        return -1