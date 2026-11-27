class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        return max(hm, key=hm.get)
        