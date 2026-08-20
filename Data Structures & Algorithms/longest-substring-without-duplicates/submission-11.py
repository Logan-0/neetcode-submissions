class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1:
            return 1
        l=0
        res=1
        cSet=set()

        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l+=1
            cSet.add(s[r])
            res = max(res, (r-l+1))
        return res