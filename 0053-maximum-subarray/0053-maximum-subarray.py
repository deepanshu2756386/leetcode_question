class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0] 
        best_ending = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            v1 = nums[i] + best_ending
            v2 = nums[i]

            best_ending = max(v1,v2)
            ans = max(best_ending, ans)

        return ans 

        