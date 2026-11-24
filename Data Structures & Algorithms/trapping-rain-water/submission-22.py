class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l < 3:
            return 0

        l1 = l2 = 0
        r1 = r2 = l - 1
        max_trapped = 0

        l1 = find_hole(l1, height, True)
        r1 = find_hole(r1, height, False)
        while l1 != r1 and r1 != 0:
            h_l1 = height[l1]
            h_r1 = height[r1]

            if h_l1 < h_r1:
                l1, max_trapped = count_left_water(l1, max_trapped, height)
            else:
                r1, max_trapped = count_right_water(r1, max_trapped, height)

            if l1 != r1:
                l1 = find_hole(l1, height, True)
                r1 = find_hole(r1, height, False)
        
        return max_trapped

def find_hole(i, height: List[int], is_left) -> int:
    if is_left:
        while height[i] <= height[i + 1] and i != len(height) - 1:
            i += 1
    else:
        while height[i] <= height[i - 1] and i != 0:
            i -= 1
    return i

def count_left_water(L, max_trapped, height: List[int]):
    R = L + 1
    h_L = height[L]

    while height[R] < h_L:
        max_trapped += (h_L - height[R])
        R += 1

    # h_R = height[R]
    # if h_R < h_L:
    #     max_trapped -= (R - L2) * (h_L - h_R)

    return R, max_trapped

def count_right_water(R, max_trapped, height: List[int]):
    L = R - 1
    h_R = height[R]

    while height[L] < h_R:
        max_trapped += (h_R - height[L])
        L -= 1

    # h_L = height[L]
    # if h_L < h_R:
    #     max_trapped -= (L - R2) * (h_R - h_L)

    return L, max_trapped
    