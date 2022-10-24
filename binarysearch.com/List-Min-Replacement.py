# https://binarysearch.com/problems/List-Min-Replacement


class Solution:
    def solve(self, nums):
        temp = [0, nums[0]]
        if len(nums) == 1:
            return nums
        # m = str(min(nums)) * (len(nums) - 2)
        m = min(nums)
        del nums[0]
        for i in range(len(nums) - 1):
            temp.append(m)
        return temp


nums = [10, 5, 7, 9]

problem = Solution()
problem.solve(nums)
