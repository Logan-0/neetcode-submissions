class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        area = 0

        while l < r:
            length = r-l
            if heights[l] > heights[r]:
                area = max(area, (length * heights[r]))
                r-=1
            else:
                area = max(area, (length * heights[l]))
                l += 1
        return area