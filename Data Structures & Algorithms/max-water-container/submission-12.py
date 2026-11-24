class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = None

        while l < r:
            h_l = heights[l]
            h_r = heights[r]

            if not area:
                area = (r - l) * min(h_l, h_r)
            elif (r - l) * min(h_l, h_r) > area:
                area = (r - l) * min(h_l, h_r)
                
            if h_l > h_r:
                r -= 1
            else:
                l += 1

        return curr_area
