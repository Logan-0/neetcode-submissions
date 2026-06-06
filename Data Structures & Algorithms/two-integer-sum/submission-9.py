class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for index, num in enumerate(nums):
            if target-num in d:
                return [d[target-num], index]
            else:
                d[num] = index
        return []