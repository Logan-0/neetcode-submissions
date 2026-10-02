class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, a in enumerate(nums):
            if target-a in d:
                return [d[target-a],i]
            else:
                d[a] = i