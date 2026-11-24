class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        h_l, h_r = heights[l], heights[r]
        curr_area = (r - l) * min(h_l, h_r)

        while l < r:
            h_l = heights[l]
            h_r = heights[r]
            if h_l < heights[l + 1]:
                l = l + 1
            
            if h_r < heights[r - 1]:
                r = r - 1
            
            h_l = heights[l]
            h_r = heights[r]

            area = (r - l) * min(h_l, h_r)
            if area > curr_area:
                curr_area = area
            
            if h_l > h_r:
                r -= 1
            else:
                l += 1

        return curr_area
