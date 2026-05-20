class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for currentIndex, currentNumber in enumerate(nums):
            
            neededNumber = target - currentNumber

            if neededNumber in d:
                return[d[neededNumber], currentIndex]

            d[currentNumber] = currentIndex

        return []