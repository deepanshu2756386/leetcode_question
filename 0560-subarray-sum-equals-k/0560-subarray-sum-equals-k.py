class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        d = {0:1}
        prev = 0
        count = 0
        for i in nums:
            prev +=i

            if prev-k in d:
                count +=d[prev-k]

            if prev in d:
                d[prev] +=1

            else:
                d[prev] = 1

        return count


        