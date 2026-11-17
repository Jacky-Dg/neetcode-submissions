class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freqs = Counter(nums)

        for num in nums:
            if freqs[num] == 1:
                return num

        
