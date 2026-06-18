class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d= dict()

        for index, number in enumerate(nums):
            if target-number in d:
                return [d[target-number], index]
            else:
                d[number] = index