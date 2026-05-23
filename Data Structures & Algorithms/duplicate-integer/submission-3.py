class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        q = set(nums)
        if len(q) != len(nums):
            return True
        return False