class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for index, number in enumerate(nums):
            if number > 0:
                break
            if index > 0 and number == nums[index-1]:
                continue
            
            l = index + 1
            r = len(nums)-1

            while l < r:
                p = number + nums[l] + nums[r]
                if p > 0:
                    r-=1
                elif p < 0:
                    l +=1
                else:
                    res.append([number, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res