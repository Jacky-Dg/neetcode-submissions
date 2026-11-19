class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = None

        while l < r:
            h_l = heights[l]
            h_r = heights[r]

            p_area = (r - l) * min(h_l, h_r)
            if not area:
                area = p_area
            elif p_area > area:
                area = p_area
                
            if h_l > h_r:
                r -= 1
            else:
                l += 1

        return area
