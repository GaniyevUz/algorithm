# https://leetcode.com/problems/reshape-the-matrix/


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        nums = []
        for i in mat:
            nums.extend(i)
        if r * c != len(nums):
            return mat

        result = []
        for i in range(r):
            result.append(nums[:c])
            nums = nums[c:]
        return result