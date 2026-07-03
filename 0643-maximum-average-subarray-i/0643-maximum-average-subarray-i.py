class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        if len(nums)< k:
            return 0
        left = 0
        window_sum =  sum(nums[:k])
        max_sum = window_sum
        
        for right  in range(len(nums)-k):
            window_sum = window_sum + nums[k+right] - nums[right]
            max_sum  = max(max_sum , window_sum)


        return float(max_sum)/k
         

            
