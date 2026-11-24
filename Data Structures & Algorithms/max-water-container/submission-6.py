class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        cl, cr = l, r
        h_l, h_r = heights[l], heights[r]
        curr_area = (r - l) * min(h_l, h_r)

        while cl < cr:
            if h_l < heights[cl + 1]:
                l = l + 1
            
            if h_r < heights[cr - 1]:
                r = r - 1
            
            h_l = heights[l]
            h_r = heights[r]

            area = (r - l) * min(h_l, h_r)
            if area > curr_area:
                curr_area = area

            if h_l > h_r:
                cr -= 1
            else:
                cl += 1

        return curr_area
