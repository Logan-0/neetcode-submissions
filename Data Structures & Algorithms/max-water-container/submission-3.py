class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        p = 0

        while l < r:
            length = r-l
            if heights[l] <= heights[r]:
                total = (heights[l] * length)
                p = max(total,p)
                l += 1
            else:
                total = (heights[r] * length)
                p = max(total,p)
                r -= 1
        return p
            