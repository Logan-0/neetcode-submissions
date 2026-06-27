class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1

        a = 0

        while l < r:
            length = r-l
            if heights[l] < heights[r]:
                a = max(a, length * heights[l])
                l += 1
            else:
                a = max(a, length * heights[r])
                r -= 1

        return a
            