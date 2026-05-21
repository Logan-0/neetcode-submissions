class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = list(set(nums))
        if len(s) == len(nums):
            return False
        return True