class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ht = {}

        for i in range(len(nums)):
            if nums[i] in ht:
                if abs(i - ht.get(nums[i])) <= k:
                    return True
            ht[nums[i]] = i

        return False