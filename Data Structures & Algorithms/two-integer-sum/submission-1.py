class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_pair = {}

        for i,v in enumerate(nums):
            diff = target - v

            if v in dict_pair:
                return [dict_pair[v], i]

            dict_pair[diff] = i;

        return [];