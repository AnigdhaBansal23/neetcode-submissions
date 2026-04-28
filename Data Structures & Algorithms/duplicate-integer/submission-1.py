class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        seen_set = set()
        for i in nums:
            if i in seen_set:
                return True
            seen_set.add(i)
        return False
