class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i =j=0
        result = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i +=1
            else:
                result.append(nums2[j])
                j +=1
        while i <len(nums1):
            result.append(nums1[i])
            i +=1
        while j<len(nums2):
            result.append(nums2[j])
            j +=1
        n = len(result)
        mid = n//2
        if n%2 ==0:
           median = (result[mid]+result[mid-1])/2.0
           return median
        else:
            median = result[mid]
            return  median


