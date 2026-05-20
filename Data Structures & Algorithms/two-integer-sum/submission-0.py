class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNumbers = {}
        for currentIndex, currentNumber in enumerate(nums):
            
            neededNumber = target - currentNumber

            if neededNumber in seenNumbers:
                return[seenNumbers[neededNumber], currentIndex]

            seenNumbers[currentNumber] = currentIndex

        return []