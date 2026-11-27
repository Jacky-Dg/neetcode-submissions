class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l < 2:
            return False

        for i in range(l):
            for j in range(i + 1, min(i + k + 1, l)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True   

        return False