class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c = [0]*len(nums)

        for i in range(len(c)):
            c[i] = i

        print(c[0])
        for num in c:
            if num not in nums:
                return num

        