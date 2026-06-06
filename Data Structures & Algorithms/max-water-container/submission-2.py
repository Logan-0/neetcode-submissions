class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        maxP = 0

        while l < r:
            length = r-l
            if heights[l] < heights[r]:
                total = heights[l] * length
                l += 1
            else:
                total = heights[r] * length
                r -= 1
            maxP = max(total, maxP)
        return maxP