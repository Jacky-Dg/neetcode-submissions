class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        nums = sorted(nums)

        while h > l:
            m = (l + h) // 2

            if m % 2 == 1:
                m -= 1

            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                h = m
        
        return nums[l]

        

        
