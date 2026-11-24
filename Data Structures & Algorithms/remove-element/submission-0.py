class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = k = len(nums)

        j = 0
        for i in range(l):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            else:
                k -= 1
        
        return k
            
