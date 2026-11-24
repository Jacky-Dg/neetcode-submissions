class Solution:
    def trap(self, height: List[int]) -> int:
        l1, l2, r = 0, 0, len(height) - 1
        max_trapped = 0
        l_trapped = 0
        while height[r] <= height[r - 1]:
            r = r - 1


        while l1 < r and l2 < r:
            while height[l1] <= height[l1 + 1]: #Find valid hole to fill water with
                l1 += 1
            l2 = l1 + 1

            while height[l1] > height[l2]: #See how much water can fill the hole
                l_trapped += height[l1] - height[l2]
                l2 += 1

            l1 = l2 #Same precondition as the beginning
            if l_trapped > max_trapped:
                max_trapped = l_trapped
        
        return max_trapped
     