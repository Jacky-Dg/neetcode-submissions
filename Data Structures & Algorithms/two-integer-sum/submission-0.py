class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = len(nums);
        for i in range(j):
            for k in range(i + 1, j):
                if ((nums[i] + nums[k]) == target):
                    return [i, k];
        return [];