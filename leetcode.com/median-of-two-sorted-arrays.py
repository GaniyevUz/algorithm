# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        n, m = len(nums1), len(nums2)
        i = j = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < n:
            result.append(nums1[i])
            i += 1
        while j < m:
            result.append(nums2[j])
            j += 1

        # with slicing uses more additional memory
        # result += nums1[i:] + nums2[j:]
        l = len(result)
        median = l // 2
        if not l % 2:
            return float((result[median - 1] + result[median]) / 2)
        return float(result[median])


num1 = [1, 3]
num2 = [2]
problem = Solution()
print(problem.findMedianSortedArrays(num1, num2))
