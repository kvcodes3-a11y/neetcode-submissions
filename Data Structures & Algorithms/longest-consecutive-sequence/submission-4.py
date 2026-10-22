class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        nums = sorted(set(nums))
        cnt = 1
        maxx = 1
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]-1):
                cnt += 1
            else:
                cnt = 1
            maxx = max(maxx, cnt)
        return maxx