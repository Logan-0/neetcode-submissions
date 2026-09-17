class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        a=0

        while l<r:
            length=r-l
            if heights[l]<heights[r]:
                a = max(a, heights[l]*length)
                l+=1
            else:
                a = max(a,heights[r]*length)
                r-=1
        return a