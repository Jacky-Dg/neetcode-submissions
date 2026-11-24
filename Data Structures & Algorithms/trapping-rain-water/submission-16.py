class Solution:
    def trap(self, height: List[int]) -> int:
        l1, l2, r1, r2 = 0, 0, len(height) - 1, len(height) - 1
        max_trapped = 0


        while l1 != r1:
            while height[l1] <= height[l1 + 1]: #Find valid hole to fill water with
                l1 += 1
            l2 = l1 + 1

            while height[r1] <= height[r1 - 1]:
                r1 = r1 - 1
            r2 = r1 - 1
            
            while height[l1] > height[l2] and l2 < r1:
                max_trapped += height[l1] - height[l2]
                l2 += 1

            l1 = l2

            if l1 != r1:
                while height[r1] > height[r2]: 
                    max_trapped += height[r1] - height[r2]
                    r2 -= 1

                r1 = r2
        return max_trapped
     