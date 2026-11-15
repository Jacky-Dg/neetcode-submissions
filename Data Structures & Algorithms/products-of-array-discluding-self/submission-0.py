class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        maxProd, maxProd2 = 1, 1
        for num in nums:
            maxProd = maxProd * num

        for i in range(len(output)):
            if not nums[i] == 0:
                output[i] = maxProd // nums[i]

            else:
                for j in range(len(nums)):
                    if not j == i:
                        maxProd2 = maxProd2 * nums[j]
                output[i] = maxProd2

        return output