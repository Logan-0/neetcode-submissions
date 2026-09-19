class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area = 0

        while l < r:
            length = r-l
            if heights[l] < heights[r]:
                v = heights[l] * length
                area = max(v, area)
                l += 1
            else:
                v = heights[r] * length
                area = max(v, area)
                r -= 1
        return area