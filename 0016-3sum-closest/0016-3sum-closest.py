class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        answer = 0
        min_closest = float("inf")
        for i  in range(len(nums)-2):
            left = i +1
            right = len(nums)-1

            while left < right:
                total = nums[i]+ nums[left] + nums[right]
                diff = abs(target - total)

                if diff < min_closest:
                    min_closest = diff
                    answer = total
                if total > target :
                    right -=1
                elif total < target:
                    left +=1
                else:
                    return total



        return answer
