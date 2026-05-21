class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for currentIndex, currentNumber in enumerate(nums):

            if target-currentNumber in d:
                return [d[target-currentNumber], currentIndex] 

            d[currentNumber] = currentIndex
