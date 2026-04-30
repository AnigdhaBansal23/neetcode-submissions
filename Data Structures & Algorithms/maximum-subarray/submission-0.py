class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -float('inf')
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            maxsum = max(current_sum,maxsum)
            if current_sum < 0:
                current_sum = 0
        return maxsum
