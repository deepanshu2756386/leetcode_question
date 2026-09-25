class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return abs(nums[0])
        max_sum = nums[0]
        min_sum = nums[0]
        res = abs(nums[0])
       
        for i in range(1,len(nums)):
            max_sum = max(nums[i],nums[i]+max_sum)
            min_sum = min(nums[i],nums[i]+min_sum)

            res = max(res , max(abs(max_sum),abs(min_sum)))

        return res
       

       

        return res 