class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(list(set(nums)))
        count=1
        res=1

        for i in range(len(nums)-1):
            if (nums[i+1] == nums[i]+1):
                count +=1
            else:
                res=max(count,res)
                count=1
        return max(count,res)