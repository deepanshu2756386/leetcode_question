class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_ending = nums[0]
        max_ending = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = nums[i]*min_ending
            v3 = nums[i]*max_ending

            max_ending = max(v1 , max(v2 , v3))
            min_ending = min(v1, min(v2,v3))

            res = max(res , max(max_ending , min_ending))

        return res 



        