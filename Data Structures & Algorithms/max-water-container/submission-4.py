class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        p = 0

        while l < r:
            length = r-l
            if heights[l] < heights[r]:
                p = max(p, heights[l]*length)
                l += 1
            else:
                p = max(p, heights[r]*length)
                r -= 1
        return p