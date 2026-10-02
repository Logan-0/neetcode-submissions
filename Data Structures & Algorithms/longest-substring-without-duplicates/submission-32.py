class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l = 0
        res = 1
        cSet = set()

        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            cSet.add(s[r])
            res = max((r-l+1), res)
        return res