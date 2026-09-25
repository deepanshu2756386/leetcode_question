class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        no_del = arr[0]
        one_del = float("-inf")
        res = arr[0]
        for i in range(1,len(arr)):
            prev_no_del = no_del 

            no_del = max(arr[i],no_del+arr[i])

            one_del = max(prev_no_del , one_del+arr[i])

            res = max(no_del , one_del , res)

        return res 
        