class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        max_ending = nums[0]
        max_sum = nums[0]

        min_ending = nums[0]
        min_sum = nums[0]

        for i in range(1, len(nums)):
            min_ending = min(nums[i], nums[i]+min_ending)
            min_sum = min(min_ending , min_sum)

            max_ending = max(nums[i], max_ending+nums[i])
            max_sum = max(max_ending, max_sum)

        if max_sum < 0:
            return max_sum 


        circular_sum  = total_sum - min_sum 

        return max(circular_sum , max_sum)

        