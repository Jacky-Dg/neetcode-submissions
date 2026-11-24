class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        cl, cr = l, r
        curr_area = (r - l) * min(heights[l], heights[r])

        while cl <= cr:
            if heights[l] < heights[cl + 1]:
                l = l + 1
            
            if heights[r] < heights[cr - 1]:
                r = r - 1

            area = (r - l) * min(heights[l], heights[r])
            if area > curr_area:
                curr_area = area
            
            cl += 1
            cr -= 1

        return curr_area
